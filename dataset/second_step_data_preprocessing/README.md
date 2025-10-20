# Data Preprocessing - Part 2

This script performs the **second phase** of the data preprocessing task for the course *“Pergaditja dhe Vizualizimi i të Dhënave.”*  
It focuses on:
- Data integration  
- Data aggregation  
- Data sampling  
- Additional data cleaning  
---

##  Description

The script loads the cleaned dataset from **Part 1**  
 `cleaned_yearwise_grant_dataset.csv`  
and performs further preprocessing to prepare it for analysis and visualization.

---

## What the Script Does

1. **Data Integration**  
   - Adds simulated state population data.  
   - Merges with the main dataset using `State name`.  
   - Saves the result as `integrated_dataset.csv`.

2. **Data Aggregation**  
   - Calculates total scholarship amount per state and year.  
   - Saves the result as `aggregated_dataset.csv`.

3. **Data Sampling**  
   - Randomly selects 5% of the dataset for testing or visualization.  
   - Saves the result as `sampled_dataset.csv`.

4. **Data Cleaning (Additional)**  
   - Removes rows with missing or invalid values.  
   - Ensures numeric columns are properly typed.  
   - Saves the result as `cleaned_part2_dataset.csv`.

---

## Dataset Info

- **Input File:** `cleaned_yearwise_grant_dataset.csv`  
- **Rows:** 43,381  
- **Columns:** 9  
- **Output Files & Shapes:**

| Output File | Description | Rows × Columns |
|-------------|------------|----------------|
| `integrated_dataset.csv` | Dataset with state population added | 43,381 × 10 |
| `aggregated_dataset.csv` | Total scholarship per state & year | 36 × 3 |
| `sampled_dataset.csv` | Random 5% sample of integrated dataset | 2,169 × 10 |
| `cleaned_part2_dataset.csv` | Cleaned dataset after removing invalid/missing values | 13,689 × 10 |

---

## Results Summary

| Step | Description | Result |
|------|------------|--------|
| Data loaded | CSV file from Part 1 read successfully | ✅ |
| Integration | Added population data | ✅ |
| Aggregation | Summarized total scholarships per state & year | ✅ |
| Sampling | Random 5% subset selected | ✅ |
| Cleaning | Missing/invalid values removed safely | ✅ |
| All outputs saved | CSV files in same directory | ✅ |

---

##  Notes

- Cleaning is performed safely to avoid pandas `SettingWithCopyWarning`.  
- Aggregated data has fewer rows because it is summarized by **Year + State**.  
- Sampling is only a small subset, intended for testing or visualization.  

---

## How to Run

Make sure the Part 1 cleaned CSV file is in the correct directory, then run:

```bash
python data_preprocessing_part2.py
