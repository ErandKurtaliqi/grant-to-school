# README – Pika 3: Explorimi i të Dhënave (EDA)

---

## 1. Qëllimi i skriptit
- Shpjegimi i shkurtër i qëllimit të eksplorimit të të dhënave
- Çka pritet të merret nga EDA?

---

## 2. Varesitë (Dependencies)
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

Instalim:
> pip install pandas numpy matplotlib seaborn

---

## 3. Strukturë projektit
- dataset/
- phase2/
- 2_Avoiding_Inaccurate_Disclosures/
- 3_Data_Exploration/
    - script_data_exploration.py
    - README.md (ky dokument)

---

## 4. Ekzekutimi i skriptit
> python script_data_exploration.py  
ose  
> python.exe script_data_exploration.py

---

## 5. Çka ndodh në skript? (shkurt me pika)

### 5.1 Leximi dhe inspektimi
- Leximi i dataset_no_outliers.csv
- Shfaq 5 rreshtat e parë
- Shfaq info të datasetit

### 5.2 Statistika përmbledhëse (Univariate)
- describe() për kolonat numerike
- histogram për amount_of_scholarship
- boxplot për amount_of_scholarship
- histogram për class

### 5.3 Analiza e variablave kategorikë
- value_counts() për state_name
- value_counts() category_name
- value_counts() aspirational_final
- value_counts() gender_male
- barplots për secilën kategori (opsionale)

### 5.4 Analiza multivariate
- groupby() për category_name dhe amount_of_scholarship (count, mean, min, max)
- groupby() aspirational_final -> mesatare
- groupby() gender_male -> mesatare
- groupby() category_name + gender_male -> mesatare
- boxplots sipas kategorive

### 5.5 Korelacion
- Convert kategori në int nëse duhen
- llogarit corr()
- shfaq heatmap

---

## 6. Rezultati final
- Përmbledhje në fund e gjetjeve nga vizualizimet dhe statistikat

---

## 7. Screenshots / Grafika
- Histogram amount_of_scholarship
- <img width="796" height="431" alt="image" src="https://github.com/user-attachments/assets/8b801de9-866e-4416-825c-c0e2505c39aa" />

- Boxplot amount_of_scholarship
- <img width="521" height="528" alt="image" src="https://github.com/user-attachments/assets/9716658a-1075-4c39-9070-04b7ccaa50d6" />
- <img width="595" height="432" alt="image" src="https://github.com/user-attachments/assets/44a34cbf-e09e-4715-b8fd-d8c6b86f6a91" />
- <img width="598" height="426" alt="image" src="https://github.com/user-attachments/assets/5b188aea-6763-4d58-acf0-ec5691785fe4" />
- <img width="399" height="494" alt="image" src="https://github.com/user-attachments/assets/32b81ee6-9621-4e84-97f5-08e9424ce4de" />
- <img width="398" height="432" alt="image" src="https://github.com/user-attachments/assets/4329a131-2b98-457e-8d82-db7f0e4cc2a9" />
- <img width="798" height="529" alt="image" src="https://github.com/user-attachments/assets/e44050c1-4989-429b-8ec5-6a6a5e8e0383" />
- <img width="598" height="533" alt="image" src="https://github.com/user-attachments/assets/da905e8f-fc6e-4f71-aeb0-76f94213ed74" />
- <img width="598" height="526" alt="image" src="https://github.com/user-attachments/assets/f42b4e48-3061-4d3d-82f3-be54272cc693" />

- Barplot kategorive
- 
- Boxplot multivariate
- Heatmap korelacioni
- <img width="600" height="427" alt="image" src="https://github.com/user-attachments/assets/af3765f9-26a5-4fe5-9b1a-3aecca028c94" />

---

