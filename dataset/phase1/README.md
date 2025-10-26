Projekti: Përgatitja dhe Vizualizimi i të Dhënave

Grupi 16

Ky projekt përfshin fazat kryesore të para-procesimit të të dhënave për pastrim, reduktim dhe analizë.
Dataset-i përfaqëson bursat e ndara për nxënësit në Indi gjatë vitit 2023.

Skriptat

01_data_cleaning_missing_outliers.py
Pastron dataset-in, trajton vlerat e zbrazëta dhe largon outliers duke përdorur metodën IQR.

02_reduction_feature_creation.py
Heq kolonat e panevojshme, normalizon të dhënat dhe krijon disa veçori të reja për analizë statistikore.

03_discretization_binarization_aggregation.py
Diskretizon kategoritë sociale me One-Hot Encoding, binarizon gjininë dhe kryen agregim sipas kategorisë.
Shton kolonën për përqindjen e bursave sipas kategorive sociale.

03_discretization_binarization_aggregation_rajone.py
Zbaton agregim shtesë sipas rajoneve dhe kategorive sociale për të analizuar shpërndarjen gjeografike të bursave.
