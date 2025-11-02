import pandas as pd
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler

def save_binarization_file_sets(df_integrated: pd.DataFrame, outputs_dir: Path) -> None:
    outputs_dir.mkdir(parents=True, exist_ok=True)
    num_keep = [c for c in ["year", "class", "amount_of_scholarship"] if c in df_integrated.columns]
    text_keep = [c for c in ["state_name", "category_name"] if c in df_integrated.columns]
    bool_keep = [c for c in ["gender", "aspirational_final"] if c in df_integrated.columns]
    small = df_integrated.loc[:, df_integrated.columns.intersection(num_keep + text_keep + bool_keep)].copy()

    if "gender" in small.columns:
        gmap = {
            "boys": True, "boy": True, "male": True, "m": True,
            "girls": False, "girl": False, "female": False, "f": False
        }
        small["gender_male"] = (
            small["gender"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map(gmap)
        ).astype("boolean")
        small = small.drop(columns=["gender"])

    if "aspirational_final" in small.columns:
        amap = {
            "aspirational": True,
            "non-aspirational": False,
            "aspirational district": True,
            "non aspirational district": False
        }
        small["aspirational_final"] = (
            small["aspirational_final"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map(amap)
        ).astype("boolean")

    if "class" in small.columns and small["class"].nunique() > 1:
        mm = MinMaxScaler()
        small[["class"]] = mm.fit_transform(small[["class"]])

    final_model_path = outputs_dir / "final_binarization_file.csv"
    small.to_csv(final_model_path, index=False)
    print(f" Final binarization + normalization saved to: {final_model_path.resolve()}")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir.parent / "3_Integration_Aggregation_Cleaning_MissingValues" / "Aggregation" / "dataset_aggregated.csv"
    output_dir = base_dir
    df = pd.read_csv(input_path)
    print("Loaded aggregated dataset:", df.shape)
    save_binarization_file_sets(df, output_dir)
