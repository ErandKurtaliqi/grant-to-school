import pandas as pd
from pathlib import Path


INPUT_FILE = Path("C:/Users/Arton/Desktop/dataset_with_exclude_detection.csv")

def explore_dataset(df, name):

    print("\nDataset:", name)
    print("--------------------------")

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(list(df.columns))

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDescriptive Statistics (Numeric):")
    print(df.describe())

    print("\nDescriptive Statistics (Categorical):")
    print(df.describe(include=['object']))


def main():
    if not INPUT_FILE.exists():
        print("Gabim: Fajlli nuk u gjet:", INPUT_FILE)
        return

    df = pd.read_csv(INPUT_FILE)
    explore_dataset(df, INPUT_FILE.name)


if __name__ == "__main__":
    main()
