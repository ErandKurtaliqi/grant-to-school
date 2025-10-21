# Data Preprocessing - Part 1

This script performs the **first phase** of the data preprocessing task for the course *“Pergaditja dhe Vizualizimi i të Dhënave.”*  
It focuses on:
- Data collection  
- Data type definition  
- Data quality checking and cleaning  
---

##  Description

The script loads the dataset  
👉 `year-wise-grant-to-school-students-of-class-6-10.csv`  
from Kaggle and performs a basic preprocessing pipeline to prepare it for later analysis.

---

## ️ What the Script Does

1. **Loads the dataset** using `pandas`.
2. **Displays**:
   - Number of rows and columns  
   - First 5 rows  
   - Data types for each column  
   - General info summary  
3. **Checks for data quality issues**:
   - Missing values  
   - Duplicate rows  
4. **Cleans the dataset**:
   - Removes duplicate rows  
   - Handles missing values (if any)  
5. **Saves** the cleaned dataset as  
   `cleaned_yearwise_grant_dataset.csv`

---

##  Dataset Info

- **Source:** [Kaggle – Year-wise Grant to School Students of Class 6–10](https://www.kaggle.com/datasets/xixama/year-wise-grant-to-school-students-of-class-6-10)  
- **Rows:** 43,381  
- **Columns:** 9  
- **File Format:** CSV  

---

##  Results Summary

| Step | Description | Result |
|------|--------------|--------|
| Data loaded | CSV file read successfully | ✅ |
| Missing values | None found | ✅ |
| Duplicates | None found | ✅ |
| Cleaned data saved | `cleaned_yearwise_grant_dataset.csv` | ✅ |

---


## How to Run

Make sure the CSV file is in the correct directory (one level above the script), then run:

```bash
python data_preprocessing_part1.py
