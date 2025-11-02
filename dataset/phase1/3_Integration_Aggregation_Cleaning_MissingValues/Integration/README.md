#  Integration

##  Objective
Ensure that the main dataset is unified and contextually complete before further processing.
If any additional information exists (e.g., region lookup), merge it here.

## ⚙ Steps Performed
1. Loaded the typed dataset from Phase 1 - Part 2.
2. Optionally checked for a regional lookup file `State_Regions.csv` and merged it.
3. Verified the resulting schema and record count.

##  Output
- **dataset_integrated.csv** – unified dataset, ready for cleaning.

##  Next Step
Used as input for **Cleaning_MissingValues/script_cleaning_missing.py**.
