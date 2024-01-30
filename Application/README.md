# HeadSpace Web Application

## Overview
HeadSpace Web Application is a cutting-edge tool designed to facilitate comparison of various vocoders within an Extended Text-to-Speech (XTTS) system. Aimed at integrating the most efficient vocoder into the "HeadSpace" TTS interface, this app focuses on assessing speech synthesis quality, naturalness, and environmental impact. The evaluation encompasses Mel Cepstral Distortion (MCD), Fundamental Frequency (F0) RMSE, Mean Opinion Score (MOS), and the carbon footprint of each vocoder's computational process.

## Features
- **Vocoder Selection**: Choose among 'HiFiGAN', 'Multi-Band MelGAN', 'WaveGrad'.
- **Upload and Synthesize**: Upload a voice sample and synthesize speech using the selected vocoder.
- **Spectrogram Visualization**: View the waveform and spectrogram of both the reference and synthesized audio.
- **Performance Metrics Display**: Analyze MCD and F0 RMSE scores through interactive charts.
- **Environmental Impact**: Assess the carbon footprint associated with the computational process of each vocoder.
- **User Interface**: Sleek, intuitive interface with pleasant responsive layout for ease of use.

## Installation
Ensure Python 3 and the necessary libraries (`torch`, `librosa`, `nicegui`, `memory_profiler`, `plotly`) are installed. Clone this repository and navigate to the app directory.

## Usage
1. **Start the Application**: Run `python3 app.py` to start the server.
2. **Vocoder Selection**: Choose a vocoder from the dropdown.
3. **Upload Voice Sample**: Click to upload voice sample and select a file.
4. **Synthesize Speech**: Click 'Synthesize' to generate speech from text input.
5. **View Results**: Check the 'Spectrogram' and 'Metrics' tabs for visual and statistical analysis.

## Technologies
- **Backend**: Python with `nicegui` for the server and GUI, `torch` for model operations.
- **Frontend**: Interactive UI with `nicegui` elements, `plotly` for graphing, and `librosa` for audio processing.
