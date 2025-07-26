# DSMTA: Deeply Supervised Multi-Task Autoencoder for Biological Brain Age Estimation

[![Official Repo](https://img.shields.io/badge/Repo-PLASS--Lab/DSMTA-blue)](https://github.com/PLASS-Lab/DSMTA)

## 🔬 About

`DSMTA` implements the Deeply Supervised Multi-Task Autoencoder (DS-MT-AE) introduced in our manuscript:

> **Title:** *Deeply Supervised Multi-Task Autoencoder for Biological Brain Age Estimation Using T1-weighted MRI*

This framework leverages:
- **Deep supervision** to stabilize optimization.  
- **Multi-task learning** for richer feature representations, jointly optimizing:
  1. **Brain age prediction**  
  2. **Sex classification**  
  3. **Image reconstruction**

## ⚙️ Features

- **Stable training** via auxiliary supervision at multiple decoder depths.  
- **Improved generalization** by coupling primary and auxiliary tasks.  
- **Easy-to-use scripts** for data preparation, training, and inference.

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

### 1. Pretrained Weights

Request access and download the pretrained model weights from:

> https://drive.google.com/drive/folders/1k8w2HuI10wOUaSyj1qPj57HHGlVUAsVz?usp=sharing

Place the files in `./weights/`.

### 2. Dataset

We use the **OpenBHB** T1-weighted MRI dataset (publicly available).

- **Raw data source:** `<DATASET_DOWNLOAD_LINK>`  
- **Processed data download:**
    ```bash
    python scripts/download_processed_data.py
    ```

This will populate:
```
├── data/
│   ├── train/    # Training images + labels
│   └── test/     # Testing images + labels
└── weights/      # Pretrained model files
```

## 🚀 Usage

### 1. Inference (Testing)

Run the inference notebook to evaluate the pretrained model:

```bash
jupyter notebook notebooks/inference_notebook.ipynb
```

### 2. Training

Explore and launch training experiments via the provided notebooks:

```bash
jupyter notebook notebooks/training/train_dsmta.ipynb
```

## 📖 Citation

If you use this code in your research, please cite:

> **Authors**, "Deeply Supervised Multi-Task Autoencoder for Biological Brain Age Estimation Using T1-weighted MRI", *Journal Name*, Year.

```bibtex
@article{your2025dsmta,
  title={Deeply Supervised Multi-Task Autoencoder for Biological Brain Age Estimation Using T1-weighted MRI},
  author={...},
  journal={Journal Name},
  year={2025}
}
```

## ⚖️ License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

<p align="center">
  <a href="https://plass.dongguk.edu" target="_blank">
    <img src="https://github.com/sucystem/PLASS/blob/main/logo.png" width="300" alt="PLASS Lab, Dongguk University">
  </a>
</p>
