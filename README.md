# DSMTA: Deeply Supervised Multi-Task Autoencoder for Biological Brain Age Estimation

[![Official Repo](https://img.shields.io/badge/Repo-PLASS--Lab/DSMTA-blue)](https://github.com/PLASS-Lab/DSMTA)

## 🔬 About

`DSMTA` provides the implementation for our manuscript:

> **Title:** *Deeply Supervised Multi-Task Autoencoder for Biological Brain Age Estimation Using T1-weighted MRI*

Key contributions:
- **Deep supervision** at multiple decoder depths for stable optimization.
- **Multi-task learning**, jointly training:
  1. Brain age prediction  
  2. Sex classification  
  3. Image reconstruction

## ⚙️ Features

- Robust training with auxiliary losses.  
- Enhanced feature representations via multitasking.  
- Ready-to-use scripts and notebooks for data prep, training, and inference.

## 📥 Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/PLASS-Lab/DSMTA.git
    cd DSMTA
    ```

2. **Create and activate Conda environment**
    ```bash
    conda create -n dsmta_env python=3.10 --file requirements.txt
    conda activate dsmta_env
    ```

## 💾 Data & Pretrained Weights

### 1. Pretrained Model Weights

Request access and download the pretrained weights:

> https://drive.google.com/drive/folders/1k8w2HuI10wOUaSyj1qPj57HHGlVUAsVz?usp=sharing

Unzip and place all files under `./weights/`.

### 2. OpenBHB Dataset

This study uses the **OpenBHB** T1-weighted MRI dataset:

- **Download link:**
  https://ieee-dataport.org/open-access/openbhb-multi-site-brain-mri-dataset-age-prediction-and-debiasing

- **Mandatory citation:**
  > Benoit Dufumier, Antoine Grigis, Julie Victor, Corentin Ambroise, Vincent Frouin, Edouard Duchesnay, “OpenBHB: a Large‑Scale Multi‑Site Brain MRI Data‑set for Age Prediction and Debiasing”, *NeuroImage*, 263:119637, 2022. doi:10.1016/j.neuroimage.2022.119637

To download our **processed** version of OpenBHB, run:
```bash
python test_data_download.py
python train_data_download.py
```
This will create the directory structure:
```
├── data/
│   ├── train/    # Training images + labels
│   └── test/     # Testing images + labels
└── weights/      # Pretrained model files
```

## 🚀 Usage

### Inference (Testing)

Launch and run the inference notebook:
```bash
jupyter notebook Inference_Notebook.ipynb
```

### Training

Open the training notebooks in the `Training_notebooks` folder:
```bash
jupyter notebook Training_notebooks/
```

## 📖 Citation

If you use this code or models in your research, please cite our paper:
```bibtex
@article{your2025dsmta,
  title={Deeply Supervised Multi-Task Autoencoder for Biological Brain Age Estimation Using T1-weighted MRI},
  author={...},
  journal={Journal Name},
  year={2025}
}
```

And when using the OpenBHB dataset, also cite:
```bibtex
@article{dufumier2022openbhb,
  title={OpenBHB: a Large-Scale Multi-Site Brain MRI Data-set for Age Prediction and Debiasing},
  author={Dufumier, Benoit and Grigis, Antoine and Victor, Julie and Ambroise, Corentin and Frouin, Vincent and Duchesnay, Edouard},
  journal={NeuroImage},
  volume={263},
  pages={119637},
  year={2022},
  doi={10.1016/j.neuroimage.2022.119637}
}
```

## ⚖️ License

Released under the **MIT License**. See [LICENSE](LICENSE) for details.

---

<p align="center">
  <a href="https://plass.dongguk.edu" target="_blank">
    <img src="https://github.com/sucystem/PLASS/blob/main/logo.png" width="300" alt="PLASS Lab, Dongguk University">
  </a>
</p>
