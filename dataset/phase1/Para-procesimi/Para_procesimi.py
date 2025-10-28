# ============================================================
# Projekti: Përgatitja dhe Vizualizimi i të Dhënave
# Autori: Grupi 16
# Dataset: Year-wise grant to school students (India, 2023)
# ============================================================

import pandas as pd

# ============================================================
# 01. Pastrimi fillestar, mbushja e vlerave që mungojnë dhe identifikimi i outliers (IQR Method)
# ============================================================

df = pd.read_csv("dataset.csv")

print("Numri fillestar i rreshtave:", len(df))
print("Kolonat ekzistuese:", list(df.columns))

# Heqja e duplikatave për të shmangur përsëritjet e panevojshme
df = df.drop_duplicates()

# Lista e kolonave tekstuale që do të pastrohen
text_cols = ['State name', 'District Name', 'Aspirational Final', 'Category name', 'Gender']

# Pastrimi i kolonave tekstuale (heqja e hapësirave dhe formatimi)
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

print("\nPastrimi i kolonave tekstuale u krye me sukses.")

# Mbushja e vlerave që mungojnë
df['Amount of Scholarship'] = df['Amount of Scholarship'].fillna(df['Amount of Scholarship'].median())
df['Category name'] = df['Category name'].fillna(df['Category name'].mode()[0])
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])

print("Vlerat që mungonin janë trajtuar me median dhe mode.")

# ============================================================
# Identifikimi dhe heqja e outliers (IQR Method)
# ============================================================

Q1 = df['Amount of Scholarship'].quantile(0.25)
Q3 = df['Amount of Scholarship'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filtrimi i të dhënave për të hequr outliers
df = df[(df['Amount of Scholarship'] >= lower_bound) & (df['Amount of Scholarship'] <= upper_bound)]

print("Kontrolli i outliers përfundoi. Nëse kishte vlera anormale, janë larguar.")
print("Numri aktual i rreshtave pas pastrimit:", len(df))

# ============================================================
#  Reduktimi i dimensionit dhe krijimi i veçorive të reja
# ============================================================

print("\n--- Faza e dytë: Reduktimi i dimensioneve dhe krijimi i veçorive ---")
print("Numri fillestar i kolonave:", len(df.columns))
print("Kolonat ekzistuese:", list(df.columns))

# Largo kolonën 'UID' nëse ekziston (identifikues teknik pa vlerë analitike)
if 'UID' in df.columns:
    df = df.drop(columns=['UID'])
    print("Kolona 'UID' u largua nga dataset-i.")

# Krijimi i veçorisë së re - përqindja e shumës së bursave sipas kategorisë sociale
category_totals = df.groupby('Category name')['Amount of Scholarship'].sum()
df['Scholarship_Category_Ratio'] = df['Category name'].map(
    lambda x: category_totals[x] / category_totals.sum()
)

print("U krijua kolona 'Scholarship_Category_Ratio' si veçori e re (feature creation).")

# ============================================================
#  Binarizimi dhe Diskretizimi i të Dhënave
# ============================================================

print("\n--- Faza e tretë: Binarizimi dhe Diskretizimi ---")
print("Numri fillestar i kolonave:", len(df.columns))
print("Kolonat ekzistuese:", list(df.columns))

# ============================================================
# Binarizimi i kolonës Gender (0 = Female, 1 = Male)
# ============================================================

# Normalizimi i vlerave të gjinisë
df['Gender'] = df['Gender'].astype(str).str.lower().str.strip()

# Krijimi i kolonës binare
df['Gender_Binary'] = df['Gender'].apply(lambda x: 1 if x in ['male', 'm'] else 0)

print("Kolona 'Gender' u binarizua me sukses (0 = Female, 1 = Male).")

# Largo kolonën origjinale pasi nuk nevojitet më
df = df.drop(columns=['Gender'])

# ============================================================
# Diskretizimi (One-Hot Encoding) për Category name
# ============================================================

category_dummies = pd.get_dummies(df['Category name'], prefix='Cat')
df = pd.concat([df, category_dummies], axis=1)
print("Kolonat e reja për kategori sociale janë krijuar me sukses (One-Hot Encoding).")

# ============================================================
# Agregimi i të dhënave sipas rajonit dhe kategorisë sociale
# ============================================================

agg = df.groupby(['State name', 'Category name'], as_index=False).agg(
    Total_Scholarships=('Amount of Scholarship', 'count'),
    Total_Amount=('Amount of Scholarship', 'sum')
)

# Largo kolonën origjinale 'Category name' nga dataset-i final
df = df.drop(columns=['Category name'])

# Krijimi i kolonës “Percentage” për përqindjen e shumës së bursave
total_amount_all = agg['Total_Amount'].sum()
agg['Percentage'] = (agg['Total_Amount'] / total_amount_all * 100).round(2)

print("\nTabela përfundimtare e agreguar sipas rajonit dhe kategorisë sociale:\n")
print(agg.head(15))

# ============================================================
# Ruajtja e rezultateve në fajlla të veçantë
# ============================================================

df.to_csv("dataset_final_processed.csv", index=False)
agg.to_csv("dataset_aggregated.csv", index=False)

print("\n Procesi përfundoi me sukses!")
print(" - 'dataset_final_processed.csv': dataset-i përfundimtar me veçori të reja dhe kolonën binare të gjinisë.")
print(" - 'dataset_aggregated.csv': tabela agreguar sipas rajonit dhe kategorisë sociale.")
