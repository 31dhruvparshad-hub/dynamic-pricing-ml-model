def create_features(df):
    df["lag_1_sales"] = (
        df.groupby("product_id")["units_sold"].shift(1)
    )

    df["lag_7_sales"] = (
        df.groupby("product_id")["units_sold"].shift(7)
    )

    df["rolling_mean_7"] = (
        df.groupby("product_id")["units_sold"]
        .rolling(7)
        .mean()
        .reset_index(level=0, drop=True)
    )

    df = df.dropna().reset_index(drop=True)
    return df
