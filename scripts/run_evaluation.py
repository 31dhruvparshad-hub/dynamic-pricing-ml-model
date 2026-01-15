import pandas as pd
from sklearn.model_selection import train_test_split
from src.train import train_models
from src.evaluate import evaluate_models

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

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    models = train_models(X_train, y_train)
    results = evaluate_models(models, X_test, y_test)

    for model, metrics in results.items():
        print(f"\n{model}")
        for k, v in metrics.items():
            print(f"{k}: {v:.2f}")

if __name__ == "__main__":
    main()
