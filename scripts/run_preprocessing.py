from src.preprocess import load_and_clean_data
from src.features import create_features

RAW_PATH = "data/raw/online_retail.csv"
PROCESSED_PATH = "data/processed/processed_data.csv"

def main():
    df = load_and_clean_data(RAW_PATH)
    df = create_features(df)
    df.to_csv(PROCESSED_PATH, index=False)
    print("Done. Processed data saved.")

if __name__ == "__main__":
    main()
