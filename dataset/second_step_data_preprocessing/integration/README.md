Data Integration - Part 3

This script performs the third phase of the data preprocessing pipeline, focusing on data integration.

It merges the aggregated scholarship data with mock external population data, creating a richer dataset that enables per-capita analysis in subsequent steps.

Description

The script loads the aggregated dataset from the previous step and integrates it with a mock external data source (state population figures) using a common key.

👉 Input File: aggregated_dataset.csv (from the aggregation step)

️ What the Script Does

Loads the dataset using pandas (it expects the input file to be one directory above its current location, matching the relative path ../aggregation/).

Creates a mock external dataset (state_population_df) containing key demographic information (Population (millions)).

Integrates the data: It performs a left merge (pd.merge) between the scholarship data and the population data based on the common key, 'State name'.

Saves the final integrated dataset as integrated_dataset.csv in the current directory.

Dataset Info

Input Source: Aggregated data from Part 2 (aggregated_dataset.csv).

Integration Data: Mock Population (millions) data (simulating an external data source).

Operation: Merging/Integration (pd.merge).

Output File: integrated_dataset.csv

New Columns: Population (millions)

Results Summary

| Step | Description | Result | |------|--------------|--------| | Data loaded | Aggregated CSV read successfully | ✅ | | Integration | Population data merged with scholarship data | ✅ | | Integrated data saved | integrated_dataset.csv | ✅ |

How to Run

Make sure the input file is in the specified relative path, then run:

python data_integration_script.py
