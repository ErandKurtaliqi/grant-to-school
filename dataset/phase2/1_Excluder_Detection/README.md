README FINAL (Copy–Paste i gatshëm për GitHub / Markdown)
# README – Skripti për Detektimin e Përjashtuesve (Outliers) me IQR

Ky skript Python kryen **detektimin e përjashtuesve (outliers)** në një dataset duke përdorur metodën **IQR (Interquartile Range)** dhe ruan rezultatin në një file të ri CSV, duke shtuar një kolonë të re `is_outlier` për secilën rresht.

---

## 1. Varësitë (Dependencies)

Për ekzekutimin e këtij skripti nevojiten paketat e mëposhtme:

- Python 3.x  
- pandas  
- numpy  
- pathlib (vjen si pjesë e standard library të Python-it)

### Instalimi i paketave të nevojshme

Nëse nuk i ke të instaluara `pandas` dhe `numpy`, mund t’i instalosh me:

```bash
pip install pandas numpy

2. Struktura e skedarëve dhe rrugët (Paths)

Skript përdor rrugë relative për input dhe output duke përdorur pathlib.Path.

from pathlib import Path

INPUT_PATH = Path("dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv")
OUTPUT_PATH = Path("dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv")

Çfarë nënkuptojnë këto rrugë?

INPUT_PATH
dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv
Ky është file-i hyrës nga i cili lexohet dataset-i. Pritet të jetë CSV i krijuar nga faza e mëparshme: Binarization & Normalization.

OUTPUT_PATH
dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv
Ky është file-i i daljes ku ruhet dataset-i me kolonën is_outlier.
Folder-i krijohet automatikisht nëse nuk ekziston.

3. Përshkrimi i plotë i skriptit

Kodi i plotë i skriptit:

import pandas as pd
import numpy as np
from pathlib import Path

INPUT_PATH = Path("dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv")
OUTPUT_PATH = Path("dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv")

df = pd.read_csv(INPUT_PATH)
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

def detect_outliers_iqr(dataframe, cols):
    outlier_mask = pd.Series(False, index=dataframe.index)

    for col in cols:
        Q1 = dataframe[col].quantile(0.25)
        Q3 = dataframe[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        col_outliers = (dataframe[col] < lower) | (dataframe[col] > upper)
        outlier_mask |= col_outliers

    return outlier_mask

df["is_outlier"] = detect_outliers_iqr(df, numeric_cols)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print("Detektimi i përjashtuesve u krye me sukses!")
print(f"Rezultati u ruajt në:\n{OUTPUT_PATH}")


Më poshtë janë shpjegimet e detajuara për çdo hap.

4. Leximi i dataset-it
df = pd.read_csv(INPUT_PATH)


Lexohet file-i CSV dhe ngarkohet në një DataFrame.

5. Përzgjedhja e kolonave numerike
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()


Përzgjidhen vetëm kolonat me tipe numerike (int, float).

6. Funksioni detect_outliers_iqr

Ky funksion detekton outliers për të gjitha kolonat numerike duke përdorur metodën IQR.

Llogaritja e kuartileve dhe IQR
Q1 = dataframe[col].quantile(0.25)
Q3 = dataframe[col].quantile(0.75)
IQR = Q3 - Q1

Kufijtë e outliers
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

Detektimi për kolonë
col_outliers = (dataframe[col] < lower) | (dataframe[col] > upper)

Kombinimi për të gjitha kolonat
outlier_mask |= col_outliers


Nëse një rresht është outlier në çfarëdo kolone → shënohet si outlier.

7. Shtimi i kolonës is_outlier
df["is_outlier"] = detect_outliers_iqr(df, numeric_cols)


Kolona e re përmban:

True → rreshti është outlier

False → rreshti është normal

8. Krijimi i folderit të output-it
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


Krijon automatikisht folderin nëse nuk ekziston.

9. Ruajtja e dataset-it të përditësuar
df.to_csv(OUTPUT_PATH, index=False)


Dataset-i ruhet në CSV pa kolonën e indeksit.

10. Mesazhet në konsol
Detektimi i përjashtuesve u krye me sukses!
Rezultati u ruajt në:
dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv

11. Si ta ekzekutoni skriptin

Sigurohu që ke instaluar python, pandas dhe numpy.

Sigurohu që ekziston file-i:

dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv


Ruaje skriptin si p.sh.:

detect_outliers_iqr.py


Ekzekuto në terminal:

python detect_outliers_iqr.py


Pas ekzekutimit krijohet file-i final:

dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv


Ky file do të përmbajë dataset-in origjinal + kolonën is_outlier.

---
