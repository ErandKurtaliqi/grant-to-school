import pandas as pd
import numpy as np

# Load the cleaned dataset from Part 1
file_path = "../first_step_data_preprocessing/cleaned_yearwise_grant_dataset.csv"
df = pd.read_csv(file_path)

print("Dataset loaded successfully.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

# -----------------------------------------------------
# 1. DATA INTEGRATION
# -----------------------------------------------------
# Simulated example: add an extra dataset with state populations
state_population_data = {
    'State name': ['Punjab', 'Rajasthan', 'Maharashtra', 'Bihar', 'Uttar Pradesh', 'Gujarat'],
    'Population (millions)': [30.0, 80.0, 125.0, 104.0, 200.0, 70.0]
}
state_population_df = pd.DataFrame(state_population_data)

# Merge both datasets based on "State name"
df_merged = pd.merge(df, state_population_df, on='State name', how='left')

print("Integration step completed. Added population data per state.\n")

# -----------------------------------------------------
# 2. DATA AGGREGATION
# -----------------------------------------------------
# Example: calculate total scholarship amount per state and year
aggregated_df = (
    df_merged.groupby(['Year', 'State name'])
    ['Amount of Scholarship']
    .sum()
    .reset_index()
    .rename(columns={'Amount of Scholarship': 'Total Scholarship Amount'})
)

print("Aggregation step completed: summarized total scholarships per state and year.\n")

# -----------------------------------------------------
# 3. DATA SAMPLING
# -----------------------------------------------------
# Randomly select 5% of the data for testing or visualization
sample_df = df_merged.sample(frac=0.05, random_state=42)
print(f"Sampling step completed. Sample size: {sample_df.shape[0]} rows.\n")

# -----------------------------------------------------
# 4. DATA CLEANING (Safer version)
# -----------------------------------------------------

# Make an explicit copy of df_merged to avoid view issues
cleaned_df = df_merged.copy()

# Remove rows with missing values in any column
cleaned_df.dropna(inplace=True)

# Ensure 'Amount of Scholarship' is numeric
cleaned_df.loc[:, 'Amount of Scholarship'] = pd.to_numeric(
    cleaned_df['Amount of Scholarship'], errors='coerce'
)

# Drop rows where 'Amount of Scholarship' became NaN after conversion
cleaned_df.dropna(subset=['Amount of Scholarship'], inplace=True)

print("Data cleaning completed safely. Missing or invalid values removed.\n")
print(f"Cleaned dataset shape: {cleaned_df.shape}")


# -----------------------------------------------------
# Save results
# -----------------------------------------------------

df_merged.to_csv("integrated_dataset.csv", index=False)
aggregated_df.to_csv("aggregated_dataset.csv", index=False)
sample_df.to_csv("sampled_dataset.csv", index=False)
cleaned_df.to_csv("cleaned_part2_dataset.csv", index=False)

print("All files saved successfully.\n")
print("Summary of Part 2:")
print(f"- Integrated dataset: {df_merged.shape}")
print(f"- Aggregated dataset: {aggregated_df.shape}")
print(f"- Sampled dataset: {sample_df.shape}")
print(f"- Cleaned dataset: {cleaned_df.shape}")
