import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_percentage_error

DATA_PATH = "data/features.csv"

def train_per_series():
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

    print(f"Average MAPE across series: {sum(mapes)/len(mapes):.2%}")

if __name__ == "__main__":
    train_per_series()

