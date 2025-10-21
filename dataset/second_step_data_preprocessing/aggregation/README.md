Data Aggregation - Part 2

This script performs the second phase of the data preprocessing pipeline, focusing on data aggregation as discussed in the course materials. It calculates the total grant amount distributed per state for each year, preparing the data for higher-level comparative analysis.

Description

The script loads the cleaned dataset from the first step and aggregates the fine-grained scholarship transaction amounts into meaningful summary statistics.

👉 Input File: cleaned_yearwise_grant_dataset.csv

️ What the Script Does

Loads the dataset using pandas (it expects the input file to be two directories above its current location, matching the relative path ../../first_step_data_preprocessing/).

Aggregates the data: It groups the data by the combination of the Year and State name columns.

Calculates the sum: It calculates the total Amount of Scholarship for each unique group.

Renames the column to Total Scholarship Amount for clarity.

Saves the newly aggregated, reduced dataset as aggregated_dataset.csv in the current directory.

Dataset Info

Input Source: Cleaned data from Part 1 (cleaned_yearwise_grant_dataset.csv).

Operation: Aggregation (groupby().sum()).

Purpose: Data Reduction and Change of Scale (from student-level to state-year level).

Output File: aggregated_dataset.csv

Output Columns: Year, State name, Total Scholarship Amount

Results Summary

Step

Description

Result

Data loaded

Cleaned CSV read successfully

✅

Aggregation

Total scholarship amount calculated by Year and State

✅

Aggregated data saved

aggregated_dataset.csv

✅

How to Run

Make sure the input file is in the specified relative path, then run:

python data_aggregation_script.py
