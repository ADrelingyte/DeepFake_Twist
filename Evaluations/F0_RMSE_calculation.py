import argparse
import numpy as np
import pyworld as pw
import soundfile as sf

def evaluate_f0_rmse(reference_path, synthesized_path, sampling_rate):
    ref_audio, _ = sf.read(reference_path)
    syn_audio, _ = sf.read(synthesized_path)

    min_length = min(len(ref_audio), len(syn_audio))
    ref_audio = ref_audio[:min_length]
    syn_audio = syn_audio[:min_length]

    ref_f0, _ = pw.dio(ref_audio, fs=sampling_rate)
    syn_f0, _ = pw.dio(syn_audio, fs=sampling_rate)

    f0_rmse = np.sqrt(np.mean((ref_f0 - syn_f0) ** 2))

    print(f"F0 RMSE: {f0_rmse:.2f} Hz")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate Fundamental Frequency (F0) RMSE between two audio files.")
    parser.add_argument("reference_path", type=str, help="Path to the reference audio file.")
    parser.add_argument("synthesized_path", type=str, help="Path to the synthesized audio file.")
    parser.add_argument("--sampling_rate", type=int, default=24000, help="Sampling rate of the audio files. Default is 24000 Hz.")

    args = parser.parse_args()

    evaluate_f0_rmse(args.reference_path, args.synthesized_path, args.sampling_rate)
