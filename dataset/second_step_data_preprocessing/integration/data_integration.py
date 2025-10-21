import pandas as pd
import numpy as np

# Load the aggregated dataset from the previous step
# Assuming the 'aggregation' directory is one level up from the current script.
file_path = "../aggregation/aggregated_dataset.csv"
try:
    df = pd.read_csv(file_path)
    print("Aggregated dataset loaded successfully for integration.")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
except FileNotFoundError:
    print(f"Error: Aggregated dataset not found at {file_path}. Please run Part 2 first.")
    # Exit gracefully if the input file is missing
    exit()

# -----------------------------------------------------
# DATA INTEGRATION - FIXING NULL VALUES
# -----------------------------------------------------

# A more comprehensive, simulated external population dataset (in millions)
# This set covers all major states found in your dataset, greatly reducing NaN values.
# Real-world data collection would ensure 100% coverage.
state_population_data = {
    'State name': [
        'Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
        'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli & Daman and Diu',
        'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
        'Jharkhand', 'Karnataka', 'Kerala', 'LAKSHADWEEP', 'Ladakh', 'Madhya Pradesh',
        'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
        'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
        'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
    ],
    # Placeholder population values (in millions) for demonstration
    'Population (millions)': [
        0.4, 49.38, 1.48, 35.6, 126.7, 1.1, 30.6, 0.5, 19.3, 1.58, 63.8, 29.5, 7.3, 13.6,
        38.5, 67.5, 35.8, 0.06, 0.3, 85.0, 125.0, 3.2, 3.4, 1.2, 2.2, 46.5, 1.6, 30.0,
        80.0, 0.69, 75.3, 37.8, 4.1, 235.0, 11.4, 98.7
    ]
}

state_population_df = pd.DataFrame(state_population_data)

# Merge aggregated data with the now comprehensive population data
# We use 'left' merge to keep all scholarship records.
integrated_df = pd.merge(df, state_population_df, on='State name', how='left')

# Check for remaining null values after fix (this should now be minimal or zero)
print("\nChecking for Null Values after Improved Integration:")
print(integrated_df.isnull().sum())

# -----------------------------------------------------
# FEATURE CREATION (Krijimi i Vetive) & TRANSFORMATION
# -----------------------------------------------------
# Create a new, meaningful feature: Grant Amount Per Capita (Per Person)
# This fulfills the "Krijimi i vetive" requirement.

# Calculation: Total Scholarship Amount / Total Population (Population in millions * 1,000,000)
# The result is the grant amount per single person.
integrated_df['Grant Per Capita'] = (
    integrated_df['Total Scholarship Amount'] / (integrated_df['Population (millions)'] * 1000000)
)

# Convert to millions for a cleaner display
integrated_df['Total Scholarship Amount (Millions)'] = integrated_df['Total Scholarship Amount'] / 1000000

# Data Transformation: Rounding Grant Per Capita for cleaner analysis and visualization
integrated_df['Grant Per Capita'] = integrated_df['Grant Per Capita'].round(4) # Round to 4 decimal places

# Drop the original large amount column to reduce dimensions (Reduktimi i dimensionit)
integrated_df.drop(columns=['Total Scholarship Amount'], inplace=True)


print("\nFeature Creation (Grant Per Capita) and Transformation (Rounding) completed successfully!")
print("New Features in Dataset:")
print(integrated_df.columns.tolist())

# Save the final integrated and featured dataset
integrated_df.to_csv("integrated_featured_dataset.csv", index=False)
print("\nIntegrated and Featured dataset saved as 'integrated_featured_dataset.csv'")
