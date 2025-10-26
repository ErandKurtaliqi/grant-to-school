import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(base_dir, "../../2_Data_Collection_Type_Definition_Quality/dataset_typed_quality_checked.csv")
output_path = os.path.join(base_dir, "dataset_integrated.csv")

df = pd.read_csv(input_path)
print("Loaded typed dataset:", df.shape)

region_file = os.path.join(base_dir, "../../../extra_data/State_Regions.csv")
if os.path.exists(region_file):
    regions = pd.read_csv(region_file)
    df = pd.merge(df, regions, on="state_name", how="left")
    print("Integrated with region mapping.")
else:
    print("ℹ️ No region file found. Proceeding without merging.")

df.to_csv(output_path, index=False)
print(f"💾 Saved integrated dataset to {output_path}")
