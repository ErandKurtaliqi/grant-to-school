import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_dir, "../Cleaning_MissingValues/dataset_cleaned.csv")
output_path = os.path.join(base_dir, "dataset_aggregated.csv")

df = pd.read_csv(input_path)
print("Loaded cleaned dataset:", df.shape)

agg = (
    df.groupby(["state_name", "gender", "category_name", "aspirational_final"])
      ["amount_of_scholarship"]
      .sum()
      .reset_index()
)

print("\n Aggregation summary (first 10 rows):")
print(agg.head(10))

# Save result
agg.to_csv(output_path, index=False)
print(f" Saved aggregated dataset to {output_path}")
