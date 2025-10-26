# 🧮 Part 2 — Data Collection, Type Definition & Quality Check

## 🎯 Objective
Ensure the dataset has consistent and valid data types, verify value quality, and identify any missing or inconsistent entries.

## ⚙️ Steps Performed
1. Loaded the preprocessed dataset (`dataset_preprocessed.csv`).
2. Defined correct data types for each field:
   - `year` → integer
   - `class` → integer
   - `amount_of_scholarship` → float
   - `gender`, `category_name`, `aspirational_final` → categorical
   - `state_name`, `district_name` → string
3. Printed missing-value summary.
4. Displayed unique values for gender, category, and aspirational labels.

## 📤 Output
- `dataset_typed_quality_checked.csv` — dataset with defined data types and quality checks completed.

## 🔗 Next Step
This file will be used by **Part 3 (Integration, Aggregation, Cleaning, Missing Values)** for deeper preprocessing and feature enrichment.
