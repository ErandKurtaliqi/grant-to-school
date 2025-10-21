import pandas as pd
import numpy as np

# Load the integrated dataset from the previous step (Part 3)
file_path = "../integration/integrated_dataset.csv"
try:
    df = pd.read_csv(file_path)
    print("Integrated dataset loaded successfully for transformation.")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
except FileNotFoundError:
    print(f"Error: Integrated dataset not found at {file_path}. Please run Part 3 first.")
    # Exit gracefully if the input file is missing
    exit()

# -----------------------------------------------------
# DATA TRANSFORMATION (Transformimi)
# -----------------------------------------------------
# Perform data smoothing by rounding the Grant Per Capita column.
# This makes the data much cleaner and easier to analyze and visualize.

# Round to 4 decimal places (two for cents, two for precision)
df['Grant Per Capita'] = df['Grant Per Capita'].round(4)

print("\nTransformation (Rounding/Smoothing) completed successfully!")

# -----------------------------------------------------
# DATA EXPLORATION (Eksplorimi i te Dhenave)
# -----------------------------------------------------
# Display the first few rows of the transformed data
print("\nFirst 5 rows of Transformed Data:")
print(df.head())

# Save the final transformed dataset
df.to_csv("transformed_dataset.csv", index=False)
print("\nTransformed dataset saved as 'transformed_dataset.csv'")
