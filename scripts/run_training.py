import pandas as pd
from src.train import train_models

DATA_PATH = "data/processed/processed_data.csv"

FEATURES = [
    "price_after_discount",
    "discount_pct",
    "competitor_diff",
    "lag_1_sales",
    "rolling_mean_7",
]

def main():
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURES]
    y = df["units_sold"]

    models = train_models(X, y)
    print("Models trained:", list(models.keys()))

if __name__ == "__main__":
    main()
