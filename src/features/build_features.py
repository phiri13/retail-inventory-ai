import pandas as pd

DATA_PATH = "data/synthetic_sales.csv"
OUTPUT_PATH = "data/features.csv"

def build_features():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    df = df.sort_values(["store_id", "product_id", "date"])

    df["lag_7"] = df.groupby(["store_id", "product_id"])["units_sold"].shift(7)
    df["lag_14"] = df.groupby(["store_id", "product_id"])["units_sold"].shift(14)
    df["rolling_mean_7"] = (
        df.groupby(["store_id", "product_id"])["units_sold"]
        .rolling(7)
        .mean()
        .reset_index(level=[0,1], drop=True)
    )

    df = df.dropna()

    df.to_csv(OUTPUT_PATH, index=False)
    print("Feature dataset generated.")

if __name__ == "__main__":
    build_features()
