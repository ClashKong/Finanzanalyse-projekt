# src/fetch_data.py

import yfinance as yf
import pandas as pd
import os

def fetch_yahoo_data(ticker: str, start="2023-01-01", end="2024-12-31"):
    """
    Ruft historische Daten von Yahoo Finance ab und speichert sie als CSV.
    """
    data = yf.download(ticker, start=start, end=end)

    # Ordner erstellen, falls er nicht existiert
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)

    # Speichern als CSV
    csv_path = f"{data_folder}/{ticker}_data.csv"
    data.to_csv(csv_path)
    print(f"Daten gespeichert unter: {csv_path}")
    return data

if __name__ == "__main__":
    df = fetch_yahoo_data("AAPL")
    print(df.head())
