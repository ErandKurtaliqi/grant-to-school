import pandas as pd
from pathlib import Path

# ---------------------------
# 1. INPUT & OUTPUT PATH
# ---------------------------

# Ky është fajlli që e ke krijuar në fazën "Detection_of_Outliers"
# ku ke kolonën is_outlier (True/False ose 0/1).
INPUT_PATH = Path(
    "dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv"
)

# Këtu do ta ruajmë dataset-in pa outliers
OUTPUT_CLEAN_PATH = Path(
    "dataset/phase2/2_Avoiding_Inaccurate_Disclosures/dataset_no_outliers.csv"
)

# Opsional: dataset vetëm me outliers (për analizë)
OUTPUT_OUTLIERS_PATH = Path(
    "dataset/phase2/2_Avoiding_Inaccurate_Disclosures/dataset_only_outliers.csv"
)

df = pd.read_csv(INPUT_PATH)

if "is_outlier" not in df.columns:
    raise ValueError(
        "Kolona 'is_outlier' nuk u gjet në dataset. "
        "Sigurohu që script_detection_outliers.py e ka krijuar këtë kolonë."
    )

outlier_mask = df["is_outlier"].astype(str).str.lower().isin(["1", "true", "yes"])

num_outliers = outlier_mask.sum()
total_rows = len(df)

print(f"Rreshta total: {total_rows}")
print(f"Rreshta të shënuar si outliers: {num_outliers}")


df_no_outliers = df[~outlier_mask].copy()

# Dataset vetëm me outliers (opsional për raportim/analizë)
df_only_outliers = df[outlier_mask].copy()

# Nëse nuk dëshiron kolonën 'is_outlier' në dataset-in e pastër, komento/hiq këtë rresht:
# df_no_outliers = df_no_outliers.drop(columns=["is_outlier"])

OUTPUT_CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)

df_no_outliers.to_csv(OUTPUT_CLEAN_PATH, index=False)
df_only_outliers.to_csv(OUTPUT_OUTLIERS_PATH, index=False)

print("✅ Mënjanimi i zbulimeve jo të sakta u krye me sukses.")
print(f"   Dataset pa outliers u ruajt në:\n   {OUTPUT_CLEAN_PATH}")
print(f"   Dataset vetëm me outliers u ruajt në:\n   {OUTPUT_OUTLIERS_PATH}")
