# DSMTA: Deeply Supervised Multi-Task Autoencoder for Biological Brain Age estimation using T1-weighted MRI
<h1 align="center"><Official Repo</strong></h1>

## About
This is the official repository of the manuscript entitled "" which propose a Deeply Supervised Multitask Autoencoder (DS-MT-AE) for brain age estimation. Our framework incorporates deep supervision to improve optimization stability and multitask learning to enhance feature representation by jointly optimizing brain age prediction with two auxiliary tasks: sex classification and image reconstruction. This repo contains suidance to create conda virtual env, downloading the pretrained weights, processed OpenBHB dataset and running test and training scripts.

## Installation of packages

```bash
# Clone the repository
git clone https://github.com/PLASS-Lab/DSMTA.git

# Navigate to the project directory
cd DSMTA

# Create Conda Env and Install dependencies
conda create -n DSMTA_env python=3.10 --file requirements.txt
conda activate DSMTA_env

```
## Downloading pretrained weights and dataset 
To download pretrained weights, download the weights from the drive link()

This study utilized OpenBHB dataset which is publicly available data and can be directly downloaded from the link () 
To download the processed dataset, please execute.
```bash
python test_data_download.py
python train_data_dataload.py

## Running testing script 

After uploading the assembly logs, collected from GDB, to the selected folder, it can be converted to a structured CSV file using `assembleyTocsv.py`

```bash
python assembleyTocsv.py
```
## Running training script 

The generated CSV file can be passed to [python-elmo](https://github.com/ThFeneuil/python-elmo) engine for power simulation.

Then, the `FeatureEngineering.py` file can be used to generate the features using a user-specified window size.

```bash
python FeatureEngineering.py
```

The refined dataset can then be used for the detection of countermeasures or disassembly using predefined feature sets and window sizes

```bash
python inference.py
python classification
```

## Features

The main features.

- **Assembly to CSV Conversion**: Convert raw assembly logs from GDB into structured CSV files, making them easier to manipulate and analyze.
- **Feature Engineering for Side-Channel Analysis**: Use `FeatureEngineering.py` to apply statistical and temporal log transformation features on the dataset, allowing for customizable feature sets and window sizes.
- **Countermeasure Detection and Disassembly Analysis**: Perform classification and disassembly tasks with the refined dataset. Experiment with different window sizes and feature sets.


## Citation
If you use this code for your research, please cite the following paper.
>Title: Enhancing deep learning-based side-channel analysis using feature engineering in a fully simulated IoT system \
>Journal: Expert Systems with Applications \
>DOI: [10.1016/j.eswa.2024.126079](https://doi.org/10.1016/j.eswa.2024.126079)
```bibtex
@article{alabdulwahab2025dlscd,
  title = {Enhancing deep learning-based side-channel analysis using feature engineering in a fully simulated IoT system},
  journal = {Expert Systems with Applications},
  volume = {266},
  pages = {126079},
  year = {2025},
  issn = {0957-4174},
  doi = {https://doi.org/10.1016/j.eswa.2024.126079},
  url = {https://www.sciencedirect.com/science/article/pii/S0957417424029464},
  author = {Alabdulwahab, Saleh and Cheong, Muyoung and Seo, Aria and Kim, Young-Tak and Son, Yunsik},
  keywords = {Side-channel attacks, Feature engineering, Hiding countermeasures, Disassembly attacks, Deep learning, Reverse engineering},
}
```

<p align="center">
  <a href="https://plass.dongguk.edu" target="_blank">
    <img src="https://github.com/sucystem/PLASS/blob/main/logo.png" width="400" alt="PLASS Lab, Dongguk University">
  </a>
</p>

