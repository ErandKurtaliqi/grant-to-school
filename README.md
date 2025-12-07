# Year-wise Grant to School Students of Class (6–10)

**Dataset Source:** [Kaggle – Year-wise Grant to School Students of Class (6–10)](https://www.kaggle.com/datasets/xixama/year-wise-grant-to-school-students-of-class-6-10)

---

## Project Overview

This project focuses on the **preprocessing and preparation of educational grant data** for students in classes 6–10.  
The dataset provides insights into year-wise grants distributed to school students, serving as a foundation for future data analysis and machine learning tasks.

In this phase, we have performed **comprehensive data preprocessing** to ensure data quality, integrity, and readiness for analytical modeling.

#### **🔎 Output After Data Cleaning (First 5 Rows)**

| Year | Student ID | State | District | Aspirational | Category | Class | Gender | Scholarship |
|------|------------|--------|-----------|--------------|----------|--------|---------|-------------|
| 2023 | 198164 | Punjab | Moga | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198165 | Rajasthan | Karauli | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198166 | Rajasthan | Sirohi | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198167 | Rajasthan | Sirohi | Aspirational | Gen | 7 | Boys | 10000 |
| 2023 | 198168 | Punjab | Firozpur | Aspirational | Gen | 8 | Boys | 10000 |

---

## Major Tasks in Data Preprocessing

### 1. Data Cleaning
We focused on improving data quality and consistency through:
- Filling in **missing values** using appropriate imputation techniques;  
- **Smoothing noisy data** to remove irregularities and inconsistencies;  
- Identifying and removing **outliers** that distort the dataset;  
- Resolving **inconsistencies** in naming, formatting, and categorical labels.

| Year | Student ID | State | District | Aspirational | Category | Class | Gender | Scholarship |
|------|------------|--------|-----------|--------------|----------|--------|---------|-------------|
| 2023 | 198164 | Punjab | Moga | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198165 | Rajasthan | Karauli | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198166 | Rajasthan | Sirohi | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198167 | Rajasthan | Sirohi | Aspirational | Gen | 7 | Boys | 10000 |
| 2023 | 198168 | Punjab | Firozpur | Aspirational | Gen | 8 | Boys | 10000 |


---

### 2. Data Reduction
To optimize performance and storage, we applied several data reduction techniques:
- **Dimensionality Reduction:** Removed redundant or less significant attributes;  
- **Numerosity Reduction:** Aggregated and summarized data to reduce record count while maintaining essential information;  
- **Data Compression:** Utilized encoding and compact formats to minimize data size.

| Year | Student ID | State | District | Aspirational | Category | Class | Gender | Scholarship |
|------|------------|--------|-----------|--------------|----------|--------|---------|-------------|
| 2023 | 198164 | Punjab | Moga | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198165 | Rajasthan | Karauli | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198166 | Rajasthan | Sirohi | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198167 | Rajasthan | Sirohi | Aspirational | Gen | 7 | Boys | 10000 |
| 2023 | 198168 | Punjab | Firozpur | Aspirational | Gen | 8 | Boys | 10000 |


---

### 3. Data Integration
We transformed and standardized data to make it more suitable for analysis:
- **Loaded the typed dataset from Phase 1 - Part 2
- **Optionally checked for a regional lookup file `State_Regions.csv` and merged it.
- **Verified the resulting schema and record count.

## Output

| Year | Student ID | State | District | Aspirational | Category | Class | Gender | Scholarship |
|------|------------|--------|-----------|--------------|----------|--------|---------|-------------|
| 2023 | 198164 | Punjab | Moga | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198165 | Rajasthan | Karauli | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198166 | Rajasthan | Sirohi | Aspirational | Gen | 6 | Boys | 10000 |
| 2023 | 198167 | Rajasthan | Sirohi | Aspirational | Gen | 7 | Boys | 10000 |
| 2023 | 198168 | Punjab | Firozpur | Aspirational | Gen | 8 | Boys | 10000 |



---

### 4. Data Aggregation
After preprocessing, **data aggregation** was performed to derive summarized views —  
combining records by year, class, and gender to identify overall trends and funding patterns.

## Output

| State Name | Gender | Category | Aspirational Final | Class | Total Scholarship |
|-------------|--------|----------|----------------------|--------|---------------------|
| Andaman and Nicobar Islands | Boys | Gen | Non-Aspirational | 6 | 10000.0 |
| Andaman and Nicobar Islands | Boys | Gen | Non-Aspirational | 7 | 10000.0 |
| Andaman and Nicobar Islands | Boys | Gen | Non-Aspirational | 8 | 10000.0 |
| Andaman and Nicobar Islands | Boys | Gen | Non-Aspirational | 9 | 10000.0 |
| Andaman and Nicobar Islands | Boys | Gen | Non-Aspirational | 10 | 10000.0 |


### 5. Binarization & Normalization
Final step that prepares data for modeling or analysis.

**Techniques applied:**
- Min–Max normalization;  
- Binary encoding (True/False → 1/0);  
- Feature scaling.

#### **🔎 Output After Binarization & Normalization (First 5 Rows)**

| State Name | Category | Aspirational Binary | Class Normalized | Scholarship | Gender Binary |
|-------------|----------|----------------------|-------------------|-------------|----------------|
| Andaman and Nicobar Islands | Gen | False | 0.00 | 10000.0 | True |
| Andaman and Nicobar Islands | Gen | False | 0.25 | 10000.0 | True |
| Andaman and Nicobar Islands | Gen | False | 0.50 | 10000.0 | True |
| Andaman and Nicobar Islands | Gen | False | 0.75 | 10000.0 | True |
| Andaman and Nicobar Islands | Gen | False | 1.00 | 10000.0 | True |


---

## Objectives
- Clean, structure, and prepare the dataset for future analysis;  
- Enable efficient visualization and trend identification;  
- Build a solid base for predictive modeling and grant distribution optimization.

---

## Repository Structure

This repository is organized into multiple folders, each representing a **specific phase** of data preprocessing.  
Every phase contains a `README.md` for documentation, a `.csv` dataset output, and a `.py` script used for that stage.

<img width="243" height="686" alt="image" src="https://github.com/user-attachments/assets/b050a7c5-745b-4b77-a70e-46fad55a8ef1" />
<img width="517" height="763" alt="image" src="https://github.com/user-attachments/assets/ea1bc8b4-a533-4fde-8a62-d44cf8add79e" />

---

## Phase Descriptions

### **1. Preprocessing for Analysis**
This folder contains the **first stage** of the pipeline.  
It ensures data consistency, removes errors, and prepares the dataset for later stages.

**Includes:**
- `script_preprocessing.py` – performs initial cleaning, encoding, and column formatting.  
- `dataset_preprocessed.csv` – cleaned dataset ready for data typing.  
- `README.md` – describes preprocessing methods and reasoning.

**Goals:**
- Remove duplicates and nulls;  
- Standardize text fields;  
- Ensure consistent column names and formats.

---

### **2. Data Collection & Type Definition**
This step defines and validates the **data schema and types**.  

**Includes:**
- `script_data_collection.py` – ensures every column has the correct type (numeric, categorical, etc.);  
- `dataset_typed_quality_checked.csv` – dataset after type correction and validation;  
- `README.md` – documents data typing and validation rules.

**Focus:**  
- Type conversions (string → int/float);  
- Detection of invalid values;  
- Structural validation of columns.

---

### **3. Integration, Aggregation & Cleaning**
This is a **multi-part phase** responsible for unifying, cleaning, and summarizing the dataset.

#### *Integration*
Merges multiple sources or datasets into a single consistent dataset.  
- Aligns schemas;  
- Removes redundancy;  
- Produces `dataset_integrated.csv`.

#### *Cleaning_MissingValues*
Handles missing and incomplete data using:
- Mean/median imputation;  
- Mode replacement for categories;  
- Removal of records with excessive missing values.  
Produces `dataset_cleaned.csv`.

#### *Aggregation*
Performs grouped aggregations by year, class, or gender.  
Summarizes total and average grant distributions.  
Produces `dataset_aggregated.csv`.

---

### **4. Binarization & Normalization**
Final step that prepares data for modeling or analysis.

**Includes:**
- `script_binarization_normalization.py` – converts categorical data to binary (0/1) and normalizes numeric features;  
- `final_binarization_file.csv` – standardized dataset ready for analysis;  
- `README.md` – explains binarization and normalization methods.

**Techniques applied:**
- Min–Max normalization;  
- One-hot encoding;  
- Feature scaling for comparability.

---

## Summary Table

| Phase | Folder | Task | Output |
|-------|---------|------|--------|
| 1 | `1_Preprocessing_for_Analysis` | Cleaning, formatting | `dataset_preprocessed.csv` |
| 2 | `2_Data_Collection_Type_Definition` | Type validation | `dataset_typed_quality_checked.csv` |
| 3 | `3_Integration_Aggregation_Cleaning` | Integration, cleaning, aggregation | `dataset_integrated.csv`, `dataset_cleaned.csv`, `dataset_aggregated.csv` |
| 4 | `4_Binarization_Normalization` | Normalization and Binarization | `final_binarization_file.csv` |

---

## Key Takeaways
- A clear **four-phase pipeline** for data preparation;  
- Clean and modular Python scripts for each transformation step;  
- Progressive improvement in **data quality and usability**;  
- Ready-to-analyze dataset suitable for statistical or ML-based exploration.

# Skripti për Detektimin e Përjashtuesve (Outliers) me IQR

# 1. Qëllimi
Ky skript ka për qëllim identifikimin e rreshtave që përmbajnë vlera statistikisht të jashtëzakonshme, të cilat duhet të përjashtohen për të garantuar saktësi të mëtejshme në analizë. Detektimi i përjashtuesve (outliers) bëhet duke përdorur metodën IQR (Interquartile Range) dhe ruan rezultatin në një CSV të ri duke shtuar kolonën is_outlier për secilën rresht.

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

# 2. Varësitë (Dependencies)

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

# 3. Struktura e skedarëve dhe rrugët (Paths)

```python
from pathlib import Path

INPUT_PATH = Path("dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv")
OUTPUT_PATH = Path("dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv")
```

Ky seksion përshkruan pse është zgjedhur strukturimi në faza (phase1, phase2), një metodë që përdoret shpesh në data pipelines, ku çdo hap prodhon një dataset të ri të gatshëm për hapin e ardhshëm.  
Përdorimi i pathlib lejon krijimin e rrugëve të sigurta që funksionojnë në çdo sistem operativ.

---

# 4. Përshkrimi i plotë i skriptit

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
print(f"Rezultati u ruajt në: \n {OUTPUT_PATH}")
```

Ky seksion përshkruan hap pas hapi se çfarë bën skripti dhe si funksionon llogjika e tij. Përfshin përshkrime të detajuara të funksionit detect_outliers_iqr dhe pse përdoret metoda IQR për detektim të vlerave të jashtëzakonshme.

---

# 5. Leximi i dataset-it

```python
df = pd.read_csv(INPUT_PATH)
```

Ky hap i lejon skriptit të ngarkojë dataset-in në memorien e programit. Dataset-i bëhet gati për analiza të mëtejshme. Përshkrimi në këtë seksion shpjegon se si pandas trajton CSV-të dhe si i identifikon tipet e kolonave.

---

# 6. Përzgjedhja e kolonave numerike

```python
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
```

Këtu përzgjidhen vetëm kolonat numerike sepse vetëm ato janë të vlefshme për llogaritjen e IQR.  
Shpjegimi i zgjeruar tregon pse kolonat kategorike ose tekstuale nuk kanë kuptim në këtë analizë.

---

# 7. Funksioni detect_outliers_iqr

Ky funksion përshkruhet në detaje: si llogariten kuartilet Q1 dhe Q3, si del vlera e IQR, pse pragjet bazohen në 1.5 × IQR, dhe si ndërtohet maska për përjashtuesit për të gjitha kolonat numerike. Shpjegohet edhe pse kjo metodë konsiderohet e qëndrueshme dhe më pak e ndikuar nga outliers sesa metodat statistikore bazuar në mesatare dhe devijim standard.

---

# 8. Shtimi i kolonës is_outlier

```python
df["is_outlier"] = detect_outliers_iqr(df, numeric_cols)
```

Ky seksion shpjegon rëndësinë e kolonës së re dhe mënyrat se si mund të përdoret në analiza të mëtejshme, nga filtrimi deri te vizualizimet.

---

# 9. Krijimi i folderit të output-it

```python
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
```

Përshkrimi tregon pse kjo linjë është kritike — shmang gabimet e ruajtjes kur folderët mungojnë dhe rrit stabilitetin e skriptit.

---

# 10. Ruajtja e dataset-it të përditësuar

```python
df.to_csv(OUTPUT_PATH, index=False)
```

Kjo pjesë shpjegon procesin e ruajtjes dhe arsyen pse kolona e indeksit nuk ruhet.

---

# 11. Mesazhet në konzol

```
Detektimi i përjashtuesve u krye me sukses!
Rezultati u ruajt në:
dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv
```

Këto mesazhe informojnë përdoruesin që gjithçka ka shkuar siç duhet.

---

# 12. Si ta ekzekutoni skriptin

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
# Eliminimi i Outliers për të Shmangur Zbulimet e Pasakta

# 1. Qëllimi i Skriptit
Përmes këtij skripti sigurohemi që analizat statistikore të mos deformohen nga vlerat ekstreme (outliers). Kjo arrihet duke ndarë dataset-in në dy pjesë të qarta: një për analiza të sigurta dhe një për hulumtim të vlerave të skajshme. Pra ky skript përpunon dataset-in e fazës 2 duke ndarë rreshtat pa outliers dhe vetëm outliers, bazuar në kolonën is_outlier të krijuar më parë nga skripti i detektimit të përjashtuesve.

## Përmbajtja

* Varësitë (Dependencies)
* Rrugët e përdorura (Paths)
* Përshkrimi i kodit
* Leximi i dataset-it
* Verifikimi i kolonës is_outlier
* Gjenerimi i filtrave për outliers
* Ndarja e dataset-it
* Ruajtja e rezultateve
* Mesazhet informative
* Si të ekzekutohet skripti

---

## 2. Varësitë (Dependencies)

Ky skript kërkon:

* Python 3.x
* pandas
* pathlib (standard library)

### Instalimi:

```
pip install pandas
```

---

## 3. Rrugët e përdorura (Paths)

Këtu përcaktohen tre rrugë:

* **INPUT_PATH** – dataset-i me `is_outlier`
* **OUTPUT_CLEAN_PATH** – dataset pa outliers
* **OUTPUT_OUTLIERS_PATH** – dataset vetëm me outliers

```python
INPUT_PATH = Path("dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv")
OUTPUT_CLEAN_PATH = Path("dataset/phase2/2_Avoiding_Inaccurate_Disclosures/dataset_no_outliers.csv")
OUTPUT_OUTLIERS_PATH = Path("dataset/phase2/2_Avoiding_Inaccurate_Disclosures/dataset_only_outliers.csv")
```

---

## 4. Përshkrimi i kodit

Skripti lexon dataset-in, kontrollon ekzistencën e kolonës `is_outlier`, pastaj ndan rreshtat në:

* dataset **pa outliers**, dhe
* dataset **vetëm me outliers**.

Në fund, i ruan të dy rezultatet në CSV të veçantë.

---

## 5. Leximi i dataset-it

```python
df = pd.read_csv(INPUT_PATH)
```

---

## 6. Verifikimi i kolonës `is_outlier`

Nëse kolona mungon, skripti ndalet.

```python
if "is_outlier" not in df.columns:
    raise ValueError("Kolona 'is_outlier' nuk u gjet në dataset...")
```

---

## 7. Gjenerimi i filtrit për outliers

Kolona pranohet në formatet: `1`, `true`, `yes` (case-insensitive).

```python
outlier_mask = df["is_outlier"].astype(str).str.lower().isin(["1", "true", "yes"])
```

Mundëson fleksibilitet ndaj formateve të ndryshme.

---

## 8. Ndarja e dataset-it

```python
df_no_outliers = df[~outlier_mask].copy()
df_only_outliers = df[outlier_mask].copy()
```

---

## 9. Ruajtja e rezultateve

Folderi krijohet automatikisht nëse mungon.

```python
OUTPUT_CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)

df_no_outliers.to_csv(OUTPUT_CLEAN_PATH, index=False)
df_only_outliers.to_csv(OUTPUT_OUTLIERS_PATH, index=False)
```

---

## 10. Mesazhet në konzol

Skripti printon:

* Numrin e rreshtave total
* Numrin e outliers
* Lokacionin e file-ve të ruajtura

---

## 11. Si të ekzekutohet skripti

1. Sigurohu që skripti i detektimit të outliers ka gjeneruar:

```
dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv
```

2. Ruaje këtë skript si:

```
avoid_inaccurate_disclosures.py
```

3. Ekzekuto:

```
python avoid_inaccurate_disclosures.py
```

4. Rezultatet do të jenë:

```
dataset/phase2/2_Avoiding_Inaccurate_Disclosures/dataset_no_outliers.csv
dataset/phase2/2_Avoiding_Inaccurate_Disclosures/dataset_only_outliers.csv
```
# Explorimi i të Dhënave (EDA)

---

## 1. Qëllimi i skriptit
- Shpjegimi i shkurtër i qëllimit të eksplorimit të të dhënave
- Çka pritet të merret nga EDA?

---

## 2. Varesitë (Dependencies)
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

Instalim:
> pip install pandas numpy matplotlib seaborn

---

## 3. Strukturë projektit
- dataset/
- phase2/
- 2_Avoiding_Inaccurate_Disclosures/
- 3_Data_Exploration/
    - script_data_exploration.py
    - README.md (ky dokument)

---

## 4. Ekzekutimi i skriptit
> python script_data_exploration.py  
ose  
> python.exe script_data_exploration.py

---

## 5. Çka ndodh në skript? (shkurt me pika)

### 5.1 Leximi dhe inspektimi
- Leximi i dataset_no_outliers.csv
- Shfaq 5 rreshtat e parë
- Shfaq info të datasetit

### 5.2 Statistika përmbledhëse (Univariate)
- describe() për kolonat numerike
- histogram për amount_of_scholarship
- boxplot për amount_of_scholarship
- histogram për class

### 5.3 Analiza e variablave kategorikë
- value_counts() për state_name
- value_counts() category_name
- value_counts() aspirational_final
- value_counts() gender_male
- barplots për secilën kategori (opsionale)

### 5.4 Analiza multivariate
- groupby() për category_name dhe amount_of_scholarship (count, mean, min, max)
- groupby() aspirational_final -> mesatare
- groupby() gender_male -> mesatare
- groupby() category_name + gender_male -> mesatare
- boxplots sipas kategorive

### 5.5 Korelacion
- Convert kategori në int nëse duhen
- llogarit corr()
- shfaq heatmap

---

## 6. Rezultati final
- Përmbledhje në fund e gjetjeve nga vizualizimet dhe statistikat

---

## 7. Screenshots / Grafika
- Histogram amount_of_scholarship
- <img width="796" height="431" alt="image" src="https://github.com/user-attachments/assets/8b801de9-866e-4416-825c-c0e2505c39aa" />

- Boxplot amount_of_scholarship
- <img width="521" height="528" alt="image" src="https://github.com/user-attachments/assets/9716658a-1075-4c39-9070-04b7ccaa50d6" />
- <img width="595" height="432" alt="image" src="https://github.com/user-attachments/assets/44a34cbf-e09e-4715-b8fd-d8c6b86f6a91" />
- <img width="598" height="426" alt="image" src="https://github.com/user-attachments/assets/5b188aea-6763-4d58-acf0-ec5691785fe4" />
- <img width="399" height="494" alt="image" src="https://github.com/user-attachments/assets/32b81ee6-9621-4e84-97f5-08e9424ce4de" />
- <img width="398" height="432" alt="image" src="https://github.com/user-attachments/assets/4329a131-2b98-457e-8d82-db7f0e4cc2a9" />
- <img width="798" height="529" alt="image" src="https://github.com/user-attachments/assets/e44050c1-4989-429b-8ec5-6a6a5e8e0383" />
- <img width="598" height="533" alt="image" src="https://github.com/user-attachments/assets/da905e8f-fc6e-4f71-aeb0-76f94213ed74" />
- <img width="598" height="526" alt="image" src="https://github.com/user-attachments/assets/f42b4e48-3061-4d3d-82f3-be54272cc693" />

- Barplot kategorive
- 
- Boxplot multivariate
- Heatmap korelacioni
- <img width="600" height="427" alt="image" src="https://github.com/user-attachments/assets/af3765f9-26a5-4fe5-9b1a-3aecca028c94" />

---

## Konkluzioni 
Puna e realizuar përfshin një proces të plotë dhe të strukturuar të përgatitjes së të dhënave, duke nisur nga detektimi i vlerave të jashtëzakonshme, eliminimi i tyre dhe përfundimisht eksplorimi statistikor i dataset-it të pastruar. Fillimisht, skripti i detektimit të outliers identifikon me saktësi rreshtat problematikë duke përdorur metodën e IQR dhe krijon një kolonë të dedikuar për të shënuar secilën vlerë të skajshme. Më pas, skripti i dytë organizon dhe ndan dataset-in në dy versionet e nevojshme: <br>
— atë të pastër dhe <br>
— atë që përmban vetëm outliers,<br>
duke siguruar që analiza e mëtejshme të jetë e saktë dhe pa devijime statistikore.

Në fazën finale, skripti i EDA-s analizon në detaje të dhënat e filtruara, duke gjeneruar statistika përmbledhëse, vizualizime dhe analiza korelacionesh që ndihmojnë në kuptimin e shpërndarjes, marrëdhënieve dhe modeleve të brendshme të dataset-it. Këto tre hapa së bashku krijojnë një pipeline të plotë dhe të mirëstrukturuar për pastrimin, validimin dhe eksplorimin e të dhënave, duke garantuar një bazë të fortë për analiza të avancuara, modelim apo vendimmarrje të mëtejshme.

