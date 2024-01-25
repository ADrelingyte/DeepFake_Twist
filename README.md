# DeepFake_Twist

# XTTS Vocoder Evaluation Project 

This project aims to systematically evaluate and compare different vocoders integrated into the Extended Text-to-Speech (XTTS) system in order to choose the best vocoder to be integrated into a working TTS interface "Headspace". The evaluation focuses on four key metrics: Mel Cepstral Distortion (MCD), Fundamental Frequency (F0) RMSE, Mean Opinion Score (MOS) based on subjective listening tests, and the carbon footprint of each vocoder's computational process.

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
3. **Objective Evaluation**: Calculate MCD and F0 RMSE for each vocoder using the synthesized outputs and ground truth.
4. **Subjective Evaluation**: Conduct MOS listening tests based on ITU-T Recommendation P.800.
5. **Carbon Footprint Analysis**: Utilize CodeCarbon to estimate the emissions generated during the synthesis process.
6. **Analysis and Comparison**: Aggregate and analyze the results to rank the vocoders based on the weighted criteria.
7. **Interface Creation and Integration**: Create the webpage in order to synthesize speech from text.

## Where & What

## 🔗 Links and Resources
| Type                            | Links                               |
| ------------------------------- | --------------------------------------- |
| 💾 **Vocoder Training**           | [TTS/README.md](https://github.com/coqui-ai/TTS/tree/dev#installation)|
| 📌 **Evaluations**                | [Main Development Plans](https://github.com/coqui-ai/TTS/issues/378)
| 🚀 **Interface**                  | [TTS Releases](https://github.com/coqui-ai/TTS/releases) and [Experimental Models](https://github.com/coqui-ai/TTS/wiki/Experimental-Released-Models)|
| 📰 **Final Report**               | [TTS Papers](https://github.com/erogol/TTS-papers)|
| 💼 **Last Presentation**          | [ReadTheDocs](https://tts.readthedocs.io/en/latest/)|
| 👩‍💻 **Sample Audios**              | [CONTRIBUTING.md](https://github.com/coqui-ai/TTS/blob/main/CONTRIBUTING.md)|



