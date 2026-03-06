# Credit Card Fraud Detection

## Project Overview
This project implements a deep learning model to detect fraudulent credit card transactions as part of SUTD DeepLearning - 50.039 course. The model aims to help credit card companies identify and prevent unauthorized charges.

## Dataset
- Source: [Kaggle Credit Card Fraud Detection Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023)
- Over 550k records from Europe 2023.
- Input Features: v1 to v28 (normalized) and transaction amount
- Output: Class label (0 = legitimate, 1 = fraudulent)

## Model Architecture
- **Type**: Binary Classification Neural Network
- **Input Layer**: Normalized features from dataset
- **Hidden Layers**: Linear layers with ReLU activation and dropout
- **Output Layer**: Linear layer with Sigmoid activation
- **Loss Function**: Binary Cross Entropy
- **Evaluation Metric**: F-1 Score

## Team Members
- Donovan Seow (1008166)
- Daniel Varun Dhanapal (1008054)

## Deliverables
- Jupyter notebook with model implementation and training
- Detailed report

## Course
50.039 Deep Learning, Y2026