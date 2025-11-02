# Part 1 — Preprocessing for Analysis

## Objective
Prepare the raw dataset for the next steps by:
- Loading it correctly
- Inspecting its structure
- Cleaning column names for consistent use in later scripts

##  Steps Performed
1. Loaded `dataset/dataset.csv` using pandas.
2. Printed dataset shape, columns, and data types.
3. Standardized column names:
   - Stripped spaces
   - Replaced spaces with underscores
   - Converted all names to lowercase

## Output
- `dataset_preprocessed.csv` — version of the dataset with standardized column names and ready for type definition.

##  Next Step
The next script (`2_Data_Collection_Type_Definition_Quality/script_data_collection.py`) will:
- Define correct data types
- Validate values
- Check for inconsistencies or missing entries.
