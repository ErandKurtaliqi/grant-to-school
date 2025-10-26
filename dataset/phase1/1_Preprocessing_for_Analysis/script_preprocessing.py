import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_dir, "../../dataset.csv")
output_path = os.path.join(base_dir, "dataset_preprocessed.csv")

df = pd.read_csv(input_path)

print(" Dataset successfully loaded.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")
print(" Columns:")
print(df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nPreview:\n", df.head())

df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

df.to_csv(output_path, index=False)
print(f"\n💾 Saved cleaned column-name dataset to {output_path}")
