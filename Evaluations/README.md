# XTTS Vocoder Evaluations

This document provides a comprehensive guide to our evaluation of different vocoders integrated into the XTTS (Extended Text-to-Speech) system. The evaluations focus on objective metrics such as Mel Cepstral Distortion (MCD), and Fundamental Frequency (F0) RMSE.

## Setup Instructions

### Requirements

Before running the evaluations, ensure you have Python installed on your system (Python 3.6 or newer is recommended). You will also need to install several Python packages listed below: 

* numpy
* scipy
* librosa
* pyworld
* soundfile

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ADrelingyte/DeepFake_Twist.git
2. Open the repository
   ```bash
   cd DeepFake_Twist
   cd Evaluations
3. Run the command depending on the metrics you would like to calculate
```bash
   python evaluate_mcd.py path/to/reference_audio.wav path/to/synthesized_audio.wav --mode plain
   python evaluate_f0_rmse.py path/to/reference_audio.wav path/to/synthesized_audio.wav --sampling_rate 24000
