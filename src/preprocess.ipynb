import pandas as pd

def load_and_clean_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["InvoiceDate"])

    # Remove invalid rows
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Rename to standard pipeline names
    df = df.rename(columns={
        "InvoiceDate": "date",
        "StockCode": "product_id",
        "UnitPrice": "base_price",
        "Quantity": "units_sold"
    })

    # Pricing-related features
    df["discount"] = 0
    df["competitor_price"] = df["base_price"] * 0.98

    df["discount_pct"] = df["discount"] / df["base_price"]
    df["price_after_discount"] = df["base_price"] - df["discount"]
    df["competitor_diff"] = df["price_after_discount"] - df["competitor_price"]

    df = df.sort_values("date").reset_index(drop=True)
    return df
