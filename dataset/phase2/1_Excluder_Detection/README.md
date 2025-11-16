# README – Skripti për Detektimin e Përjashtuesve (Outliers) me IQR

Ky skript Python kryen **detektimin e përjashtuesve (outliers)** në një dataset duke përdorur metodën **IQR (Interquartile Range)** dhe ruan rezultatin në një file të ri CSV, duke shtuar një kolonë të re `is_outlier` për secilën rresht.

---

## 1. Varësitë (Dependencies)

Për ekzekutimin e këtij skripti nevojiten paketat e mëposhtme:

- [Python 3.x](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- `pathlib` (vjen si pjesë e standard library të Python-it)

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

Ky është file-i hyrës (input) nga i cili lexohet dataset-i.

Pritet të jetë një file CSV i përfunduar nga faza e mëparshme: Binarization & Normalization.

OUTPUT_PATH
dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv

Ky është file-i i daljes (output) ku do të ruhet dataset-i me kolonën shtesë is_outlier.

Folder-i dataset/phase2/1_Excluder_Detection/ do të krijohet automatikisht nëse nuk ekziston.

Sigurohu që struktura e folderëve dataset/phase1/4_Binarization_Normalization/ ekziston dhe që file-i final_binarization_file.csv është i pranishëm aty.

3. Përshkrimi i plotë i skriptit

Kodi i plotë:

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


Më poshtë është shpjegimi 100% i detajuar, rresht për rresht dhe koncept për koncept.

4. Leximi i dataset-it
df = pd.read_csv(INPUT_PATH)


Përdoret pandas.read_csv për të lexuar file-in CSV.

df do të jetë një DataFrame që përmban të gjitha kolonat dhe rreshtat e dataset-it hyrës.

Nëse rruga nuk ekziston ose file-i mungon, Python do të hedhë një gabim (FileNotFoundError).

5. Përzgjedhja e kolonave numerike
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()


df.select_dtypes(include=[np.number]):

Filtron vetëm kolonat që janë të tipit numerik (p.sh. int64, float64, etj.).

.columns.tolist():

Merr emrat e këtyre kolonave dhe i kthen si listë Python-i (list[str]).

Rezultati, numeric_cols, është një listë me emrat e të gjitha kolonave numerike mbi të cilat do të aplikojmë detektimin e përjashtuesve.

Shembull konceptual:

numeric_cols = ["age", "height", "weight", "score", ...]

6. Funksioni detect_outliers_iqr

Funksioni kryesor që bën të gjithë punën e detektimit të përjashtuesve është:

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

6.1. Parametrat

dataframe: një pandas.DataFrame (në rastin tonë df) që përmban të dhënat.

cols: një listë me emra kolonash numerike (në rastin tonë numeric_cols).

6.2. Krijimi i maskës fillestare
outlier_mask = pd.Series(False, index=dataframe.index)


Krijohet një Series booleane me gjatësi sa numri i rreshtave në dataframe.

Vlerat fillestare janë të gjitha False → duke nënkuptuar që në fillim presupozohen asnjë rresht si outlier.

index=dataframe.index siguron që indeksi i kësaj maske përputhet saktësisht me indeksin e DataFrame-it.

6.3. Llogaritja e IQR për secilën kolonë

Për çdo kolonë numerike kryhen këto hapa brenda for col in cols:

Q1 = dataframe[col].quantile(0.25)
Q3 = dataframe[col].quantile(0.75)
IQR = Q3 - Q1


Q1 – kuartili i parë (25%):

Vlera nën të cilën bie 25% i të dhënave.

Q3 – kuartili i tretë (75%):

Vlera nën të cilën bie 75% i të dhënave.

IQR = Q3 - Q1:

Gama ndërkuartile (Interquartile Range) → tregon intervalin ku bie 50% i mesëm i të dhënave.

6.4. Kufijtë për detektimin e outliers
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR


lower – kufiri i poshtëm:

Çdo vlerë më e vogël se ky kufi konsiderohet outlier në fund (lower outlier).

upper – kufiri i sipërm:

Çdo vlerë më e madhe se ky kufi konsiderohet outlier në krye (upper outlier).

Koeficienti 1.5 është standard në metodologjinë klasike të IQR për detektimin e outliers. (Mund të ndryshohet nëse duam detektim më të ndjeshëm ose më konservativ.)

6.5. Ndërtimi i maskës për një kolonë të vetme
col_outliers = (dataframe[col] < lower) | (dataframe[col] > upper)


Kjo krijon një Series booleane:

True → nëse vlera në atë rresht është < lower ose > upper.

False → përndryshe.

6.6. Kombinimi i rezultateve për të gjitha kolonat
outlier_mask |= col_outliers


Përdoret operatori logjik OR me pranim (|=) mbi outlier_mask.

Nëse një rresht është outlier në cilëndo prej kolonave numerike, ai rresht shënohet True në outlier_mask.

Pra:

Në fund të loop-it, outlier_mask[i] == True nëse rreshti i ka të paktën një vlerë outlier në ndonjë kolonë të listës cols.

6.7. Vlera e kthyer
return outlier_mask


Funksioni kthen një pandas.Series me dtype=bool:

indeksi → njësoj me dataframe.index

vlerat → True ose False (outlier / jo-outlier)

7. Shtimi i kolonës is_outlier në DataFrame
df["is_outlier"] = detect_outliers_iqr(df, numeric_cols)


Thirret funksioni detect_outliers_iqr duke i kaluar:

df – dataset-i të plotë

numeric_cols – lista e kolonave numerike

Rezultati është një Series booleane që i shtohet si kolonë e re në DataFrame me emrin is_outlier.

Përmbajtja e kolonës is_outlier:

True → rreshti është përjashtues (ka të paktën një vlerë jashtë kufijve IQR në ndonjë kolonë numerike).

False → rreshti nuk është detektuar si përjashtues në asnjë kolonë numerike.

Shembull (konceptual):

col1	col2	col3	is_outlier
10	5	7	False
200	6	8	True
12	99	9	True
8. Krijimi i folderit të output-it nëse nuk ekziston
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


OUTPUT_PATH.parent → merr folder-in prind të path-it të output-it, dmth:
dataset/phase2/1_Excluder_Detection/

.mkdir(parents=True, exist_ok=True):

parents=True → krijon të gjithë folderët prind nëse mungojnë.

exist_ok=True → nëse folderi ekziston, mos ço gabim, thjesht vazhdo.

Ky hap siguron që skripti nuk do të dështojë për shkak të mungesës së folderit të output-it.

9. Ruajtja e dataset-it të përditësuar
df.to_csv(OUTPUT_PATH, index=False)


Ruhet DataFrame df (tani me kolonën shtesë is_outlier) në rrugën:

dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv

index=False:

Nuk ruhet kolona e indeksit të DataFrame-it në CSV.

CSV do të përmbajë vetëm kolonat e dataset-it origjinal + is_outlier.

10. Mesazhet në konsol
print("Detektimi i përjashtuesve u krye me sukses!")
print(f"Rezultati u ruajt në:\n{OUTPUT_PATH}")


Mesazhi i parë tregon se procesi i detektimit të outliers është kryer me sukses.

Mesazhi i dytë tregon saktësisht se ku është ruajtur rezultati (me rrugën relative të output-it).

Shembull output në terminal:

Detektimi i përjashtuesve u krye me sukses!
Rezultati u ruajt në:
dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv

11. Si ta ekzekutoni skriptin

Sigurohu që ke instaluar python, pandas dhe numpy.

Sigurohu që file-i:

dataset/phase1/4_Binarization_Normalization/final_binarization_file.csv
ekziston dhe është i lexueshëm.

Ruaje kodin në një file, p.sh. detect_outliers_iqr.py.

Nga terminali (në root të projektit ku është vendosur folderi dataset/), ekzekuto:

python detect_outliers_iqr.py


Pas ekzekutimit të suksesshëm:

Do të gjenerohet file-i:

dataset/phase2/1_Excluder_Detection/dataset_with_exclude_detection.csv

Ky file do të përmbajë të gjitha kolonat origjinale + kolonën is_outlier.