# save_binarization_file_sets

Ky funksion pastron, binarizon dhe normalizon disa kolona nga një dataset i integruar dhe e ruan rezultatin si CSV për përdorim në modelim ose analiza të mëtejshme.

---

## Çfarë bën funksioni?

1. **Zgjedh kolonat e rëndësishme (nëse ekzistojnë):**
   - Numerike: `year`, `class`, `amount_of_scholarship`
   - Tekst: `state_name`, `category_name`
   - Booleane/Label: `gender`, `aspirational_final`

2. **Binarizon `gender` në `gender_male`** dhe heq kolonën origjinale.
3. **Binarizon `aspirational_final`** në `boolean`.
4. **Normalizon kolonat numerike** me `MinMaxScaler` (në intervalin 0-1).
5. **Ruaj rezultatin** si `final_binarization_file.csv` në `outputs_dir`.

---

## Hyrjet & Daljet

**Hyrje:**
- `df_integrated` *(pd.DataFrame)* — dataset me kolonat e sipërpërmendura.
- `outputs_dir` *(Path)* — direktoria ku do të ruhet CSV-ja.

**Dalje:**
- `final_binarization_file.csv` (CSV pa indeks).

---

## Binarizimi i kolonave

### `gender` → `gender_male`
| Vlera hyrëse | Rezultati |
|---------------|------------|
| boys, boy, male, m | True |
| girls, girl, female, f | False |
| tjetër | <NA> |

### `aspirational_final`
| Vlera hyrëse | Rezultati |
|---------------|------------|
| aspirational, aspirational district | True |
| non-aspirational, non aspirational district | False |
| tjetër | <NA> |

---

## Normalizimi i kolonave numerike

- Nëse kolona ka më shumë se një vlerë unike → aplikohet `MinMaxScaler()`.
- Përndryshe, kthehet në `float`.

---

## Skedari i daljes 

- Emri: `final_binarization_file.csv`
- Vendndodhja: `outputs_dir`
- Formati: CSV (`index=False`)

---

## Varësitë

- pandas  
- scikit-learn  
- python ≥ 3.8

Importet bazë:
```python
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler

