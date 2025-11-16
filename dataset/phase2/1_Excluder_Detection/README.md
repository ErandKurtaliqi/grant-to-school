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

---

# 1. Varësitë (Dependencies)

Për ekzekutimin e këtij skripti nevojiten paketat:

- Python 3.x
- pandas
- numpy
- pathlib *(standard library e Python-it)*

Ky seksion shpjegon se pse këto biblioteka janë të nevojshme dhe si funksionon secila në kontekst të detektimit të outliers.  
Pandas është e domosdoshme sepse mundëson manipulimin e dataset-it, leximin e CSV-ve, filtrimin dhe krijimin e kolonave të reja.  
Numpy përdoret për identifikimin e kolonave numerike dhe për operacione matematikore të brendshme që pandas mbështetet.  
Pathlib siguron një mënyrë moderne dhe të sigurt për të menaxhuar rrugët e skedarëve, duke shmangur probleme të zakonshme të sintaksës në rrugët string.

### Instalimi i paketave:
```bash
pip install pandas numpy
```

---

# 2. Struktura e skedarëve dhe rrugët (Paths)

```python
from pathlib import Path

INPUT_PATH = Path("dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv")
OUTPUT_PATH = Path("dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv")
```

Ky seksion përshkruan pse është zgjedhur strukturimi në faza (phase1, phase2), një metodë që përdoret shpesh në data pipelines, ku çdo hap prodhon një dataset të ri të gatshëm për hapin e ardhshëm.  
Përdorimi i pathlib lejon krijimin e rrugëve të sigurta që funksionojnë në çdo sistem operativ.

---

# 3. Përshkrimi i plotë i skriptit

Kodi i plotë i skriptit:

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
print(f"Rezultati u ruajt në:
{OUTPUT_PATH}")
```

Ky seksion përshkruan hap pas hapi se çfarë bën skripti dhe si funksionon llogjika e tij. Përfshin përshkrime të detajuara të funksionit detect_outliers_iqr dhe pse përdoret metoda IQR për detektim të vlerave të jashtëzakonshme.

---

# 4. Leximi i dataset-it

```python
df = pd.read_csv(INPUT_PATH)
```

Ky hap i lejon skriptit të ngarkojë dataset-in në memorien e programit. Dataset-i bëhet gati për analiza të mëtejshme. Përshkrimi në këtë seksion shpjegon se si pandas trajton CSV-të dhe si i identifikon tipet e kolonave.

---

# 5. Përzgjedhja e kolonave numerike

```python
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
```

Këtu përzgjidhen vetëm kolonat numerike sepse vetëm ato janë të vlefshme për llogaritjen e IQR.  
Shpjegimi i zgjeruar tregon pse kolonat kategorike ose tekstuale nuk kanë kuptim në këtë analizë.

---

# 6. Funksioni detect_outliers_iqr

Ky funksion përshkruhet në detaje: si llogariten kuartilet Q1 dhe Q3, si del vlera e IQR, pse pragjet bazohen në 1.5 × IQR, dhe si ndërtohet maska për përjashtuesit për të gjitha kolonat numerike. Shpjegohet edhe pse kjo metodë konsiderohet e qëndrueshme dhe më pak e ndikuar nga outliers sesa metodat statistikore bazuar në mesatare dhe devijim standard.

---

# 7. Shtimi i kolonës is_outlier

```python
df["is_outlier"] = detect_outliers_iqr(df, numeric_cols)
```

Ky seksion shpjegon rëndësinë e kolonës së re dhe mënyrat se si mund të përdoret në analiza të mëtejshme, nga filtrimi deri te vizualizimet.

---

# 8. Krijimi i folderit të output-it

```python
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
```

Përshkrimi tregon pse kjo linjë është kritike — shmang gabimet e ruajtjes kur folderët mungojnë dhe rrit stabilitetin e skriptit.

---

# 9. Ruajtja e dataset-it të përditësuar

```python
df.to_csv(OUTPUT_PATH, index=False)
```

Kjo pjesë shpjegon procesin e ruajtjes dhe arsyen pse kolona e indeksit nuk ruhet.

---

# 10. Mesazhet në konzol

```
Detektimi i përjashtuesve u krye me sukses!
Rezultati u ruajt në:
dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv
```

Këto mesazhe informojnë përdoruesin që gjithçka ka shkuar siç duhet.

---

# 11. Si ta ekzekutoni skriptin

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
