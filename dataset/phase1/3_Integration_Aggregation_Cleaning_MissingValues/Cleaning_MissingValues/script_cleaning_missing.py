import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_dir, "../Integration/dataset_integrated.csv")
output_path = os.path.join(base_dir, "dataset_cleaned.csv")

df = pd.read_csv(input_path)
print("Loaded integrated dataset:", df.shape)

missing = df.isnull().sum()
print("\nMissing values before cleaning:\n", missing)

if "district_name" in df.columns:
    df["district_name"].fillna("Unknown District", inplace=True)
if "state_name" in df.columns:
    df = df[df["state_name"].notnull()]

df = df.drop_duplicates()

# Fix invalid numeric entries
if "amount_of_scholarship" in df.columns:
    df = df[df["amount_of_scholarship"] >= 0]

print("\nAfter cleaning:\n", df.isnull().sum())

df.to_csv(output_path, index=False)
print(f"Saved cleaned dataset to {output_path}")
