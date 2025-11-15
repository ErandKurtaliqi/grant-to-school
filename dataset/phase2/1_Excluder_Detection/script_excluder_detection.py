import pandas as pd
import numpy as np
from pathlib import Path

# ---------------------------
# INPUT & OUTPUT PATH
# ---------------------------
INPUT_PATH = Path("C:/Users/Erand Kurtaliqi/OneDrive/Desktop/Master/Pergatitja dhe Vizualizimi i te dhenave/Information_Security/grant-to-school/dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv")

OUTPUT_PATH = Path("C:/Users/Erand Kurtaliqi/OneDrive/Desktop/Master/Pergatitja dhe Vizualizimi i te dhenave/Information_Security/grant-to-school/dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv")

# ---------------------------
# 1. Leximi i CSV-së
# ---------------------------
df = pd.read_csv(INPUT_PATH)




# Gjej kolonat numerike
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# ---------------------------
# 2. Funksioni për detektimin e outliers me IQR
# ---------------------------
def detect_outliers_iqr(dataframe, cols):
    outlier_mask = pd.Series(False, index=dataframe.index)

    for col in cols:
        Q1 = dataframe[col].quantile(0.25)
        Q3 = dataframe[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        col_outliers = (dataframe[col] < lower) | (dataframe[col] > upper)
        outlier_mask |= col_outliers  # kombinim i outliers në të gjitha kolonat

    return outlier_mask

# ---------------------------
# 3. Llogaritja e OUTLIERS
# ---------------------------
df["is_outlier"] = detect_outliers_iqr(df, numeric_cols)

# ---------------------------
# 4. Ruajtja e rezultatit në CSV
# ---------------------------
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)  # krijon folderat nëse mungojnë
df.to_csv(OUTPUT_PATH, index=False)

print("✔ Detektimi i përjashtuesve u krye me sukses!")
print(f"✔ Rezultati u ruajt në:\n{OUTPUT_PATH}")
