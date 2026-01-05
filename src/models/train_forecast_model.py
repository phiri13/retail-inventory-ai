import os
import pandas as pd
import joblib
from prophet import Prophet
from sklearn.metrics import mean_absolute_percentage_error

DATA_PATH = "data/features.csv"
MODEL_DIR = "models/prophet"

os.makedirs(MODEL_DIR, exist_ok=True)

def train_and_save_models():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    df = df.rename(columns={"date": "ds", "units_sold": "y"})

    mapes = []

    for (store, product), group in df.groupby(["store_id", "product_id"]):
        train = group[group["ds"] < "2023-11-01"]
        test = group[group["ds"] >= "2023-11-01"]

        if len(train) < 60 or len(test) < 7:
            continue

        model = Prophet(
            weekly_seasonality=True,
            yearly_seasonality=True
        )
        model.fit(train[["ds", "y"]])

        forecast = model.predict(test[["ds"]])
        mape = mean_absolute_percentage_error(test["y"], forecast["yhat"])
        mapes.append(mape)

        model_path = f"{MODEL_DIR}/{store}_{product}.pkl"
        joblib.dump(model, model_path)

    print(f"Average MAPE across series: {sum(mapes)/len(mapes):.2%}")
    print(f"Saved {len(mapes)} models to {MODEL_DIR}")

if __name__ == "__main__":
    train_and_save_models()

