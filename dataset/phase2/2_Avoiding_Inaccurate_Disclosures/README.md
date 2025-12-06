# README – Eliminimi i Outliers për të Shmangur Zbulimet e Pasakta

## 1. Qëllimi i Skriptit
Përmes këtij skripti sigurohemi që analizat statistikore të mos deformohen nga vlerat ekstreme (outliers). Kjo arrihet duke ndarë dataset-in në dy pjesë të qarta: një për analiza të sigurta dhe një për hulumtim të vlerave të skajshme.
Pra ky skript përpunon dataset-in e fazës 2 duke ndarë rreshtat **pa outliers** dhe **vetëm outliers**, bazuar në kolonën `is_outlier` të krijuar më parë nga skripti i detektimit të përjashtuesve.

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

