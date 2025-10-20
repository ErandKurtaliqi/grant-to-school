# ==========================================================
# Project: Data Preparation and Visualization - Part 1
# Tasks: Data Collection, Data Type Definition, Data Quality Assessment
# Dataset: Year-wise grant to school students of class (6–10)
# ==========================================================

import pandas as pd

# 1. Data Collection
# Replace the path below with the path to your dataset
file_path = "../dataset.csv"

# Load dataset
df = pd.read_csv(file_path)

print("Dataset successfully loaded.")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}\n")

print("First 5 rows of the dataset:")
print(df.head(), "\n")

# 2. Definition of Data Types
print("Data types for each column:")
print(df.dtypes, "\n")

# Optional: Convert columns to the correct types (if necessary)
# Example: Convert 'Year' to int, 'Class' to string
df['Year'] = df['Year'].astype(int)
df['Class'] = df['Class'].astype(str)

# Show info summary
print("Dataset information summary:")
print(df.info(), "\n")

# 3. Data Quality Assessment
print("Checking for missing values:")
print(df.isnull().sum(), "\n")

print("Checking for duplicate rows:")
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}\n")

# Remove duplicate rows if any
if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicate rows removed.\n")

# Handle missing values
# Option 1: Drop rows with missing values
df_cleaned = df.dropna()

# Option 2 (alternative): Fill missing numeric values with the column mean
# df_cleaned['Amount'] = df['Amount'].fillna(df['Amount'].mean())

print("After cleaning:")
print(f"Rows: {df_cleaned.shape[0]}, Columns: {df_cleaned.shape[1]}")
print("Remaining missing values per column:")
print(df_cleaned.isnull().sum(), "\n")

# 4. Export the cleaned dataset
cleaned_path = "cleaned_yearwise_grant_dataset.csv"
df_cleaned.to_csv(cleaned_path, index=False)
print(f"Cleaned dataset saved as: {cleaned_path}")

# 5. Summary
print("\nSummary of Data Cleaning:")
print(f"- Original dataset: {df.shape[0]} rows")
print(f"- Cleaned dataset: {df_cleaned.shape[0]} rows")
print("- Missing values handled")
print("- Duplicate rows removed")
print("- Data types verified\n")

print("Part 1 completed successfully.")
