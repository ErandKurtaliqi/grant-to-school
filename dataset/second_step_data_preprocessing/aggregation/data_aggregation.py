import pandas as pd

# Load the cleaned dataset from Part 1
file_path = "../../first_step_data_preprocessing/cleaned_yearwise_grant_dataset.csv"
df = pd.read_csv(file_path)

print("Dataset loaded successfully for aggregation.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# -----------------------------------------------------
# DATA AGGREGATION
# -----------------------------------------------------
# Calculate total scholarship amount per state and year
aggregated_df = (
    df.groupby(['Year', 'State name'])['Amount of Scholarship']
    .sum()
    .reset_index()
    .rename(columns={'Amount of Scholarship': 'Total Scholarship Amount'})
)

print("\nAggregation completed successfully!")
print(f"Aggregated dataset shape: {aggregated_df.shape}")

# Save aggregated dataset
aggregated_df.to_csv("aggregated_dataset.csv", index=False)
print("\nAggregated dataset saved as 'aggregated_dataset.csv'")
