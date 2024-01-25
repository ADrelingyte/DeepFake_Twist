# DeepFake_Twist

# XTTS Vocoder Evaluation Project

This project aims to systematically evaluate and compare different vocoders integrated into the Extended Text-to-Speech (XTTS) system. The evaluation focuses on four key metrics: Mel Cepstral Distortion (MCD), Fundamental Frequency (F0) RMSE, Mean Opinion Score (MOS) based on subjective listening tests, and the carbon footprint of each vocoder's computational process.

## Objective

To identify the vocoder that provides the best balance between speech synthesis quality, naturalness, and environmental impact within the XTTS framework.

## Evaluation Criteria

- **Mel Cepstral Distortion (MCD)**: Measures the spectral distortion between the synthesized and reference audio signals.
- **Fundamental Frequency (F0) RMSE**: Assesses the accuracy of the pitch in synthesized speech compared to the reference.
- **Mean Opinion Score (MOS)**: Subjective quality rating of the synthesized speech's naturalness, collected from naïve listeners.
- **Carbon Footprint**: Estimates the CO2 emissions associated with the computational resources used by each vocoder.

## Methodology

1. **Data Preparation**: Download the data.
2. **Vocoder Training**: Train each vocoder on a multilingual dataset.
3. **Objective Evaluation**: Calculate MCD and F0 RMSE for each vocoder using the synthesized outputs.
4. **Subjective Evaluation**: Conduct MOS listening tests based on ITU-T Recommendation P.800.
5. **Carbon Footprint Analysis**: Utilize CodeCarbon to estimate the emissions generated during the synthesis process.
6. **Analysis and Comparison**: Aggregate and analyze the results to rank the vocoders based on the weighted criteria.

## Installation and Usage

Describe the steps for setting up the project environment, including installing XTTS, the vocoders, and any dependencies for analysis (e.g., `librosa`, `pyworld`, `soundfile`, `CodeCarbon`).

```bash
# Example installation commands
pip install librosa pyworld soundfile codecarbon
