# README – Pika 3: Explorimi i të Dhënave (EDA)

---

## 1. Qëllimi i skriptit
- [ ] Shpjegimi i shkurtër i qëllimit të eksplorimit të të dhënave
- [ ] Çka pritet të merret nga EDA?

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
- [ ] Leximi i dataset_no_outliers.csv
- [ ] Shfaq 5 rreshtat e parë
- [ ] Shfaq info të datasetit

### 5.2 Statistika përmbledhëse (Univariate)
- [ ] describe() për kolonat numerike
- [ ] histogram për amount_of_scholarship
- [ ] boxplot për amount_of_scholarship
- [ ] histogram për class

### 5.3 Analiza e variablave kategorikë
- [ ] value_counts() për state_name
- [ ] value_counts() category_name
- [ ] value_counts() aspirational_final
- [ ] value_counts() gender_male
- [ ] barplots për secilën kategori (opsionale)

### 5.4 Analiza multivariate
- [ ] groupby() për category_name dhe amount_of_scholarship (count, mean, min, max)
- [ ] groupby() aspirational_final -> mesatare
- [ ] groupby() gender_male -> mesatare
- [ ] groupby() category_name + gender_male -> mesatare
- [ ] boxplots sipas kategorive

### 5.5 Korelacion
- [ ] Convert kategori në int nëse duhen
- [ ] llogarit corr()
- [ ] shfaq heatmap

---

## 6. Rezultati final
- [ ] Përmbledhje në fund e gjetjeve nga vizualizimet dhe statistikat

---

## 7. Screenshots / Grafika
> Këtu i fut vetë imazhet:
- [ ] Histogram amount_of_scholarship
- [ ] Boxplot amount_of_scholarship
- [ ] Barplot kategorive
- [ ] Boxplot multivariate
- [ ] Heatmap korelacioni

---

