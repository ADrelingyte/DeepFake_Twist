#!/usr/bin/env python3
import os
from nicegui import run, ui
from nicegui.events import UploadEventArguments
from memory_profiler import profile
import torch
from TTS.api import TTS
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import nicegui.binding
import gc
import plotly.graph_objects as go

# Increase threshold for binding propagation warning from 0.01 to 0.02 seconds
nicegui.binding.MAX_PROPAGATION_TIME = 0.3

VOCODERS = ['HiFiGAN', 'Multi-Band MelGAN', 'WaveGrad']
VOC_PATH = ['./vocoders/hifi.pth', './vocoders/multi.pth', './vocoders/wavegrad.pth']
VOC_CONF_PATH = ['./vocoders/hifi.json', './vocoders/multi.json', './vocoders/wavegrad.json']

output_file_path = os.getcwd() + '/tmp/output.wav'  
sample_file_path = os.getcwd() + '/tmp/uploaded_voice_sample.wav' 
save_path_syn = './tmp/visualization_syn.png' 
save_path_ref = './tmp/visualization_ref.png' 


tts_model = None

@profile
def load_tts_model():
    global tts_model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if tts_model is None:
        tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2", vocoder_path= VOC_PATH[select_voc.value], vocoder_config_path= VOC_CONF_PATH[select_voc.value]).to(device)
        print(VOC_PATH[select_voc.value], VOC_CONF_PATH[select_voc.value])
    gc.collect()
    return tts_model


@profile
async def plot_audio(file_path, save_path):

    y, sr = librosa.load(file_path)
    
    if y is not None and sr is not None:
        plt.figure(figsize=(12, 8), dpi=80)

        plt.subplot(2, 1, 1) 
        plt.plot(np.linspace(0, len(y) / sr, num=len(y)), y)
        plt.title('Waveform')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')

        plt.subplot(2, 1, 2) 
        S = librosa.feature.melspectrogram(y=y, sr=sr)
        S_DB = librosa.power_to_db(S, ref=np.max)
        librosa.display.specshow(S_DB, sr=sr, x_axis='time', y_axis='mel')
        plt.title('Mel Spectrogram')
        plt.colorbar(format='%+2.0f dB')

        plt.subplots_adjust(hspace=0.5) 

        plt.savefig(save_path)
        plt.close()
        gc.collect()
    else:
        print("Error loading audio file.")


@profile
def tts(e: UploadEventArguments):
    output_audio.visible = False
    temp_filename = os.getcwd() + '/tmp/uploaded_voice_sample.wav'
    with open(temp_filename, 'wb') as f:
        f.write(e.content.read())
    gc.collect()

@profile
def voice_cloning():
    global tts_model
    if tts_model is None:
        tts_model = load_tts_model()
    tts_model.tts_to_file(text=prompt.value, speaker_wav= os.getcwd() + "/tmp/uploaded_voice_sample.wav", language=select_lang.value, file_path= os.getcwd() + "/tmp/output.wav")
    del tts_model
    tts_model = None
    if torch.cuda.is_available():
        torch.cuda.empty_cache()  
    gc.collect()

async def start_computation():
    spinner.visible = True
    await run.cpu_bound(voice_cloning)
    spinner.visible = False
    with audio_section:
        output_audio = ui.audio(os.getcwd() + '/tmp/output.wav')
        output_audio.visible = True
    with sample_section:
        sample = ui.audio(os.getcwd() + '/tmp/uploaded_voice_sample.wav').classes('place-content-center')
        sample.visible = True
    with syn_section:
        syn = ui.audio(os.getcwd() + '/tmp/output.wav').classes('place-content-center')
        syn.visible = True
    ui.notify('Speech synthesis completed')
    gc.collect()


async def build_plot():
    await plot_audio(sample_file_path, save_path_ref)
    await plot_audio(output_file_path, save_path_syn)
    plot_syn.force_reload()
    plot_syn.visible = True
    plot_ref.force_reload()
    plot_ref.visible = True
    ui.notify('Plot is completed')
    gc.collect()


def change_mode(dark):
    if dark.value:
        ui.colors()
        dark.disable()
    else:
        ui.colors(primary='#555')
        dark.enable()




#ui.query('body').style(f"background-image: url('https://i.ibb.co/6JdKQgg/back.png')")

with ui.header():
    with ui.column().classes('w-full justify-center'):
        with ui.element().classes('w-full justify-center'):
            with ui.tabs().classes('w-full justify-center') as tabs:
                tts_tab = ui.tab('TTS', icon='code')
                wave = ui.tab('Spectrogram', icon='graphic_eq')
                specs = ui.tab('Metrics', icon='bar_chart' )
                info = ui.tab('Timeline', icon='event')
        with ui.element().classes('w-full justify-center'):
            with ui.row().classes('w-full'):
                dark = ui.dark_mode()
                mode_icon = ui.icon('thumb_up').classes('text-2xl')
                #mode_button = ui.button('txt', on_click= lambda: mode_button.)
                ui.switch('', on_change= lambda: change_mode(dark))
                ui.space()
                

with ui.tab_panels(tabs, value=tts_tab).classes('w-full h-full'):
    with ui.tab_panel(tts_tab):
        with ui.card().classes('fixed-center'): 
            with ui.row().classes('w-full justify-center').style('gap:15em'):
                with ui.column():
                    ui.label('Upload voice sample:').classes('text-2xl')
                    ui.upload(on_upload= tts, auto_upload=True).style('width: 20em')
                    with ui.row():
                        ui.button('Synthesize', icon ='swap_vert', on_click=lambda: start_computation())
                        spinner = ui.spinner(size='lg')
                        spinner.visible = False
                    with ui.element() as audio_section:
                        output_audio = ui.audio(output_file_path)
                        output_audio.visible = False
                            
                with ui.column():
                    ui.label('Text to voice').classes('text-2xl')
                    with ui.row():
                        prompt = ui.textarea(label='Text', placeholder='start typing')
                        select_lang = ui.select(['en','es', 'fr', 'de', 'it', 'nl', 'pt', 'pl', 'tr', 'ru'], value= 'en')
                        select_voc = ui.select({0: 'HiFiGAN', 1: 'Multi-Band MelGAN', 2: 'WaveGrad'}, value=0)
    
   
    with ui.tab_panel(wave):
        with ui.card().classes('w-full'): 
            with ui.column().classes('w-full justify-center no-wrap').style('gap:2em'): 
                with ui.row().classes('w-full justify-center no-wrap'):
                    ui.button('Plot Spectrogram', icon='troubleshoot', on_click= lambda: build_plot()).classes('w-80').classes('shadow-lg')
                with ui.row().classes('w-full justify-center no-wrap').style('gap:30em'):
                    with ui.card():
                        ui.label('Reference Sample:').classes('text-2xl')
                        with ui.element() as sample_section:
                            sample = ui.audio(sample_file_path).classes('place-content-center')
                            sample.visible = False
                    with ui.card():
                        ui.label('Synthesized Sample:').classes('text-2xl')
                        with ui.element() as syn_section:
                            syn = ui.audio(output_file_path)
                            syn.visible = False
            with ui.card().classes('w-full').style('align-items: center;'):
                with ui.splitter().style('width: 1200px; height: 800px;') \
                        .props('before-class=overflow-hidden after-class=overflow-hidden') as splitter:
                    with splitter.before:
                        plot_ref = ui.image(save_path_ref).style('width: 1200px; height: 800px; position: absolute; top: 0; left: 0;')
                        plot_ref.visible = False
                    with splitter.after:
                        plot_syn = ui.image(save_path_syn).style('width: 1200px; height: 800px; position: absolute; top: 0; right: 0;')
                        plot_syn.visible = False

    with ui.tab_panel(info):
        with ui.timeline(side='right'):
            ui.timeline_entry('Encountered some issues with our cluster grid5000, GPU drivers not compatible with the necessary package versions. Timeline included small training trial runs.',
                            title='Downloading the datasets & Installing requirement',
                            subtitle='September-October, 2023')
            ui.timeline_entry('Vocoders trained up to 300 000 steps, evaluating their quality subjectively along the way and monitoring loss. Encountered some internal package errors, reformatted the dataloader.',
                            title='Training of the Vocoders',
                            subtitle='October-Decembe, 2023')
            ui.timeline_entry('Started building the Interface, and evaluating the audios. Conducted MCD, F0_RMSE, MOS and Carbon Emission tests.',
                            title='Evaluation & Interface',
                            subtitle='December-January, 2024'
                            )
            ui.timeline_entry('Today',
                            title='Presentation day',
                            subtitle='February 25, 2024',
                            icon='rocket')
    with ui.tab_panel(specs):
        with ui.row().classes('w-full justify-center no-wrap'):
            with ui.card().classes('w-1/2'):
                ui.label('French MCD Scores by Vocoder').classes('text-2xl')
                echart = ui.echart({
                    'xAxis': {'type': 'value'},
                    'yAxis': {'type': 'category', 'data': ['MCD Scores'], 'inverse': True},
                    'legend': {'textStyle': {'color': 'gray'}},
                    'series': [
                        {'type': 'bar', 'name': 'Hifigan', 'data': [23.12037395627331]},
                        {'type': 'bar', 'name': 'Multiband Melgan', 'data': [22.245349153418047]},
                        {'type': 'bar', 'name': 'Wavegrad', 'data': [23.549868964709674]},
                    ],
                })
            with ui.card().classes('w-1/2'):
                ui.label('F0 RMSE Scores by Vocoder').classes('text-2xl')
                echart = ui.echart({
                    'xAxis': {'type': 'value'},
                    'yAxis': {'type': 'category', 'data': ['F0 RMSE Scores'], 'inverse': True},
                    'legend': {'textStyle': {'color': 'gray'}},
                    'series': [
                        {'type': 'bar', 'name': 'Hifigan', 'data': [134.01]},
                        {'type': 'bar', 'name': 'Multiband Melgan', 'data': [140.55]},
                        {'type': 'bar', 'name': 'Wavegrad', 'data': [161.40]},
                    ],
                }).tooltip('Chart')
        with ui.card().classes('w-full'):
            fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 2.5]))
            fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
            ui.plotly(fig).classes('w-full h-80')

            
if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
    gc.collect()