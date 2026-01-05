import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

START_DATE = "2023-01-01"
DAYS = 365
STORES = ["JHB_01", "CPT_01", "DBN_01"]
PRODUCTS = ["BREAD", "MILK", "RICE"]

def is_payday(date):
    return date.day in [25, 26, 27]

def generate_data():
    rows = []
    start = datetime.strptime(START_DATE, "%Y-%m-%d")

    for day in range(DAYS):
        current_date = start + timedelta(days=day)
        for store in STORES:
            for product in PRODUCTS:
                base_demand = np.random.randint(20, 50)

                if is_payday(current_date):
                    base_demand *= 1.3

                if current_date.weekday() >= 5:
                    base_demand *= 1.1

                load_shedding_stage = np.random.choice([0, 1, 2, 3], p=[0.4, 0.3, 0.2, 0.1])
                base_demand *= (1 - load_shedding_stage * 0.05)

                rows.append({
                    "date": current_date.date(),
                    "store_id": store,
                    "product_id": product,
                    "units_sold": int(base_demand),
                    "price": np.random.uniform(10, 30),
                    "is_weekend": current_date.weekday() >= 5,
                    "is_payday": is_payday(current_date),
                    "load_shedding_stage": load_shedding_stage
                })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/synthetic_sales.csv", index=False)
    print("Synthetic retail data generated.")
