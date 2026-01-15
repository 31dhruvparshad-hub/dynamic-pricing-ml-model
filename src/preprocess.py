import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path, parse_dates=["date"])

    df["discount_pct"] = df["discount"] / df["base_price"]
    df["price_after_discount"] = df["base_price"] - df["discount"]
    df["competitor_diff"] = df["price_after_discount"] - df["competitor_price"]

    df = df.sort_values("date")
    df = df.dropna()

    return df
