Data Transformation - Part 4

This script performs the fourth and final phase of the initial data preprocessing task for Phase I, focusing on Data Transformation (Transformimi).

It addresses the long decimal values inherited from the feature creation step, making the data cleaner and ready for statistical analysis and visualization.

Description

The script loads the integrated dataset and applies a smoothing transformation to the key analytical column, Grant Per Capita, by rounding the values. This fulfills the final requirement of Phase I.

👉 Input File: integrated_dataset.csv (from the integration/feature creation step)

️ What the Script Does

Loads the dataset using pandas.

Data Transformation (Transformimi): It applies the .round(4) function to the Grant Per Capita column to smooth the data, making it suitable for analysis and visualization.

Explorimi i të Dhënave (Data Exploration): Displays the first 5 rows to confirm the transformation.

Saves the final, clean dataset as transformed_dataset.csv.

Dataset Info

Input Source: integrated_dataset.csv

Transformed Column: Grant Per Capita

Output File: transformed_dataset.csv

Results Summary

Step

Description

Result

Data loaded

Integrated CSV read successfully

✅

Transformation

Grant Per Capita rounded (smoothed)

✅

Data saved

transformed_dataset.csv

✅

How to Run

Ensure the integrated_dataset.csv file exists in the correct relative path.

Run the script:

python data_transformation_part_4.py
