# Credit Card Fraud Detection

## Project Overview
This project implements a deep learning model to detect fraudulent credit card transactions as part of SUTD DeepLearning - 50.039 course. The model aims to help credit card companies identify and prevent unauthorized charges.

## Dataset
- Source: [Kaggle Credit Card Fraud Detection Dataset 2023](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- 492 Frauds out of 284,807 transactions (0.17% fraud).
- Input Features: v1 to v28 (normalized) and transaction amount
- Output: Class label (0 = legitimate, 1 = fraudulent)

## Model Architecture
- **Type**: Binary Classification Neural Network
- **Input Layer**: Normalized features from dataset
- **Hidden Layers**: Linear layers with ReLU activation 
- **Output Layer**: Dropout before Linear layer
- **Loss Function**: Binary Cross Entropy with Logits Loss
- **Evaluation Metrics**: F-1 Score, Precision and AUC-ROC

## Team Members
- Donovan Seow (1008166)
- Daniel Varun Dhanapal (1008054)

## Deliverables
- Jupyter notebook with model implementation and training
- Detailed report

## Course
50.039 Deep Learning, Y2026


## Load Pretrained Model

To reproduce exact results:

### Steps

1. Clone repository:

```
https://github.com/killerdolp/Deep-learning-credit-card-fraud-detection.git
```

2. Run all code blocks in:

```
pretrainedModel.ipynb
```

### Required Files

Located in `Training_weights/`:

* `amount_scaler.pkl`
* `model_weights.pth`



## Reproducibility Instructions to train the weights

### 1. Install Dependencies

```bash
pip install torch torchmetrics numpy pandas matplotlib scikit-learn imbalanced-learn
```

### 2. Download Dataset

* Source: Kaggle Credit Card Fraud Detection (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
* Save as:

```
creditcard.csv
```

### 3. Data Splitting

* Run all code blocks in:

```
split_data.ipynb
```

* Output: 3 CSV files (train/val/test)

### 4. Train Model

* Run all code blocks in:

```
Training_weights/modelfromscratch.ipynb
```

---

