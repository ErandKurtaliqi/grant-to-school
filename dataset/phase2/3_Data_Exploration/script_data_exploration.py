import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def main():
    print("=== LEXIMI I DATASETIT ===")
    df = pd.read_csv(r"dataset\phase2\2_Avoiding_Inaccurate_Disclosures\dataset_no_outliers.csv")

    print("\n--- 5 rreshtat e parë ---")
    print(df.head())

    print("\n=== INFO E DATASETIT ===")
    print(df.info())

    numeric_cols = ["class", "amount_of_scholarship"]
    numeric_cols = [c for c in numeric_cols if c in df.columns]

    if numeric_cols:
        print("\n=== STATISTIKA PËRMBLEDHËSE PËR VARIABLAT NUMERIKË ===")
        print(df[numeric_cols].describe())
    else:
        print("\n[KUJDES] Nuk u gjetën kolonat numerike të pritura në dataset.")

    if "amount_of_scholarship" in df.columns:
        plt.figure(figsize=(8, 4))
        plt.hist(df["amount_of_scholarship"], bins=30)
        plt.title("Histogram i amount_of_scholarship (pa outliers)")
        plt.xlabel("Shuma e bursës")
        plt.ylabel("Frekuenca")
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(4, 5))
        plt.boxplot(df["amount_of_scholarship"], vert=True)
        plt.title("Boxplot i amount_of_scholarship (pa outliers)")
        plt.ylabel("Shuma e bursës")
        plt.tight_layout()
        plt.show()

    if "class" in df.columns:
        plt.figure(figsize=(6, 4))
        plt.hist(df["class"], bins=10)
        plt.title("Histogram i klasës")
        plt.xlabel("class")
        plt.ylabel("Frekuenca")
        plt.tight_layout()
        plt.show()

    cat_cols = ["state_name", "category_name", "aspirational_final", "gender_male"]
    cat_cols = [c for c in cat_cols if c in df.columns]

    print("\n=== FREKUENCAT PËR VARIABLAT KATEGORIKË ===")

    if "state_name" in df.columns:
        print("\nNumri i shteteve të ndryshme:")
        print(df["state_name"].nunique())

        print("\nTop 10 shtetet sipas numrit të rasteve:")
        print(df["state_name"].value_counts().head(10))

    if "category_name" in df.columns:
        print("\nFrekuencat për category_name:")
        print(df["category_name"].value_counts())

        plt.figure(figsize=(6, 4))
        df["category_name"].value_counts().plot(kind="bar")
        plt.title("Frekuencat e kategorive (category_name)")
        plt.xlabel("category_name")
        plt.ylabel("Numri i rasteve")
        plt.tight_layout()
        plt.show()

    if "aspirational_final" in df.columns:
        print("\nFrekuencat për aspirational_final:")
        print(df["aspirational_final"].value_counts())

        plt.figure(figsize=(4, 4))
        df["aspirational_final"].value_counts().plot(kind="bar")
        plt.title("Frekuencat e aspirational_final")
        plt.xlabel("aspirational_final")
        plt.ylabel("Numri i rasteve")
        plt.tight_layout()
        plt.show()

    if "gender_male" in df.columns:
        print("\nFrekuencat për gender_male:")
        print(df["gender_male"].value_counts())

        plt.figure(figsize=(4, 4))
        df["gender_male"].value_counts().plot(kind="bar")
        plt.title("Frekuencat e gender_male")
        plt.xlabel("gender_male")
        plt.ylabel("Numri i rasteve")
        plt.tight_layout()
        plt.show()

    if "category_name" in df.columns and "amount_of_scholarship" in df.columns:
        print("\n=== STATISTIKA SË BASHKU PËR amount_of_scholarship SIPAS category_name ===")
        group_cat = df.groupby("category_name")["amount_of_scholarship"].agg(
            ["count", "mean", "median", "min", "max"]
        )
        print(group_cat)

    if "aspirational_final" in df.columns and "amount_of_scholarship" in df.columns:
        print("\n=== MESATARJA E amount_of_scholarship SIPAS aspirational_final ===")
        group_asp = df.groupby("aspirational_final")["amount_of_scholarship"].mean()
        print(group_asp)

    if "gender_male" in df.columns and "amount_of_scholarship" in df.columns:
        print("\n=== MESATARJA E amount_of_scholarship SIPAS gender_male ===")
        group_gender = df.groupby("gender_male")["amount_of_scholarship"].mean()
        print(group_gender)

    if (
        "category_name" in df.columns
        and "gender_male" in df.columns
        and "amount_of_scholarship" in df.columns
    ):
        print("\n=== MESATARJA E amount_of_scholarship SIPAS category_name DHE gender_male ===")
        group_cat_gender = df.groupby(["category_name", "gender_male"])[
            "amount_of_scholarship"
        ].mean()
        print(group_cat_gender)

    if "category_name" in df.columns and "amount_of_scholarship" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df, x="category_name", y="amount_of_scholarship")
        plt.title("Shpërndarja e bursës sipas category_name")
        plt.xlabel("category_name")
        plt.ylabel("amount_of_scholarship")
        plt.tight_layout()
        plt.show()

    if "aspirational_final" in df.columns and "amount_of_scholarship" in df.columns:
        plt.figure(figsize=(6, 5))
        sns.boxplot(data=df, x="aspirational_final", y="amount_of_scholarship")
        plt.title("Shpërndarja e bursës sipas aspirational_final")
        plt.xlabel("aspirational_final")
        plt.ylabel("amount_of_scholarship")
        plt.tight_layout()
        plt.show()

    if "gender_male" in df.columns and "amount_of_scholarship" in df.columns:
        plt.figure(figsize=(6, 5))
        sns.boxplot(data=df, x="gender_male", y="amount_of_scholarship")
        plt.title("Shpërndarja e bursës sipas gjinisë (gender_male)")
        plt.xlabel("gender_male")
        plt.ylabel("amount_of_scholarship")
        plt.tight_layout()
        plt.show()

    cols_for_corr = []
    for c in ["class", "amount_of_scholarship", "aspirational_final", "gender_male"]:
        if c in df.columns:
            cols_for_corr.append(c)

    if cols_for_corr:
        df_corr = df.copy()

        for col in ["aspirational_final", "gender_male"]:
            if col in df_corr.columns:
                df_corr[col] = df_corr[col].astype(int)

        corr_matrix = df_corr[cols_for_corr].corr()

        print("\n=== MATRICA E KORELACIONIT PËR VARIABLAT NUMERIKË ===")
        print(corr_matrix)

        plt.figure(figsize=(6, 4))
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Matrica e korelacionit")
        plt.tight_layout()
        plt.show()
    else:
        print("\n[KUJDES] Nuk ka mjaft variabla numerikë për të llogaritur korelacionin.")

    print("\n>>> EDA u kry me sukses!")

if __name__ == "__main__":
    main()