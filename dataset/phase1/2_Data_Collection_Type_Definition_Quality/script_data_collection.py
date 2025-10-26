import pandas as pd
import os

input_path = "../1_Preprocessing_for_Analysis/dataset_preprocessed.csv"
output_path = "dataset_typed_quality_checked.csv"

df = pd.read_csv(input_path)
print(" Loaded preprocessed dataset.")
print(df.info())

type_mappings = {
    "year": "int64",
    "class": "int64",
    "amount_of_scholarship": "float64",    "gender": "category",
    "category_name": "category",
    "state_name": "string",
    "district_name": "string",
    "aspirational_final": "category"
}

for col, dtype in type_mappings.items():
    if col in df.columns:
        df[col] = df[col].astype(dtype, errors="ignore")

print("\n Data types defined successfully.")

missing_values = df.isnull().sum()
print("\n Missing Values per Column:\n", missing_values)

if "gender" in df.columns:
    print("\nUnique Genders:", df["gender"].unique())
if "category_name" in df.columns:
    print("Unique Categories:", df["category_name"].unique())
if "aspirational_final" in df.columns:
    print("Unique Aspirational Labels:", df["aspirational_final"].unique())

df.to_csv(output_path, index=False)
print(f"\n Saved typed and quality-checked dataset to {output_path}")
