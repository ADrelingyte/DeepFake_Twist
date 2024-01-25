import argparse
from pymcd.mcd import Calculate_MCD

def evaluate_mcd(reference_path, synthesized_path, mode):
    mcd_toolbox = Calculate_MCD(MCD_mode=mode)
    mcd_value = mcd_toolbox.calculate_mcd(synthesized_path, reference_path)
    print(f"MCD Value ({mode} mode): {mcd_value:.2f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate Mel Cepstral Distortion (MCD) between two audio files.")
    parser.add_argument("reference_path", type=str, help="Path to the reference audio file.")
    parser.add_argument("synthesized_path", type=str, help="Path to the synthesized audio file.")
    parser.add_argument("--mode", type=str, choices=["plain", "dtw", "dtw_sl"], default="plain",
                        help="MCD calculation mode: 'plain', 'dtw', or 'dtw_sl'. Default is 'plain'.")

    args = parser.parse_args()
    evaluate_mcd(args.reference_path, args.synthesized_path, args.mode)
