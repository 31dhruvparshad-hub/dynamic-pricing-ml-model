def create_features(df):
    df["lag_1_sales"] = df["units_sold"].shift(1)
    df["lag_7_sales"] = df["units_sold"].shift(7)
    df["rolling_mean_7"] = df["units_sold"].rolling(7).mean()

    df = df.dropna()
    return df
