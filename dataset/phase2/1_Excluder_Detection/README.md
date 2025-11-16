# README – Skripti për Detektimin e Përjashtuesve (Outliers) me IQR

Ky skript Python kryen detektimin e përjashtuesve (outliers) në një dataset duke përdorur metodën **IQR (Interquartile Range)** dhe ruan rezultatin në një CSV të ri duke shtuar kolonën `is_outlier` për secilën rresht.

## Përmbajtja

- Varësitë (Dependencies)
- Struktura e skedarëve dhe rrugët (Paths)
- Përshkrimi i plotë i skriptit
- Leximi i dataset-it
- Përzgjedhja e kolonave numerike
- Funksioni detect_outliers_iqr
- Shtimi i kolonës is_outlier
- Krijimi i folderit të output-it
- Ruajtja e dataset-it të përditësuar
- Mesazhet në konzol
- Si ta ekzekutoni skriptin

## 1. Varësitë (Dependencies)

Për ekzekutimin e këtij skripti nevojiten paketat:

- Python 3.x
- pandas
- numpy
- pathlib *(standard library e Python-it)*

### Instalimi i paketave:
```bash
pip install pandas numpy
```

## 2. Struktura e skedarëve dhe rrugët (Paths)

```python
from pathlib import Path

INPUT_PATH = Path("dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv")
OUTPUT_PATH = Path("dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv")
```

## 3. Përshkrimi i plotë i skriptit

```python
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
```

## 4. Leximi i dataset-it

```python
df = pd.read_csv(INPUT_PATH)
```

## 5. Përzgjedhja e kolonave numerike

```python
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
```

## 6. Funksioni detect_outliers_iqr

Përdor metodën IQR për të detektuar outliers.

## 7. Shtimi i kolonës is_outlier

```python
df["is_outlier"] = detect_outliers_iqr(df, numeric_cols)
```

## 8. Krijimi i folderit të output-it

```python
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
```

## 9. Ruajtja e dataset-it të përditësuar

```python
df.to_csv(OUTPUT_PATH, index=False)
```

## 10. Mesazhet në konsol

```
Detektimi i përjashtuesve u krye me sukses!
Rezultati u ruajt në:
dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv
```

## 11. Si ta ekzekutoni skriptin

1. Sigurohu që ekziston file-i input:
   ```
   dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv
   ```

2. Ruaje skriptin si:
   ```
   detect_outliers_iqr.py
   ```

3. Ekzekuto:
   ```bash
   python detect_outliers_iqr.py
   ```

4. Output-i gjendet në:
   ```
   dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv
   ```
