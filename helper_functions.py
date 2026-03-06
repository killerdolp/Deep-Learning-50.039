
import numpy as np
import pandas as pd

def load_creditcard_dataset(excel_file_path="creditcard_2023.csv"):
    
    df = pd.read_csv(excel_file_path)
    V1 = df['V1'].values
    V2 = df['V2'].values
    V3 = df['V3'].values
    V4 = df['V4'].values
    V5 = df['V5'].values
    V6 = df['V6'].values
    V7 = df['V7'].values
    V8 = df['V8'].values
    V9 = df['V9'].values
    V10 = df['V10'].values
    V11 = df['V11'].values
    V12 = df['V12'].values
    V13 = df['V13'].values
    V14 = df['V14'].values
    V15 = df['V15'].values
    V16 = df['V16'].values
    V17 = df['V17'].values
    V18 = df['V18'].values
    V19 = df['V19'].values
    V20 = df['V20'].values
    V21 = df['V21'].values
    V22 = df['V22'].values
    V23 = df['V23'].values
    V24 = df['V24'].values
    V25 = df['V25'].values
    V26 = df['V26'].values
    V27 = df['V27'].values
    V28 = df['V28'].values
    amount = df['Amount'].values
    y = df['Class'].values
    x = np.column_stack([V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28])
    return V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, amount, x, y
