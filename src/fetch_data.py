import yfinance as yf
import pandas as pd
import os

def fetch_yahoo_data(ticker: str, start="2023-01-01", end="2024-12-31"):
    """
    Ruft historische Daten von Yahoo Finance ab und speichert sie als CSV.
    """
    data = yf.download(ticker, start=start, end=end)

    # 🔥 Stelle sicher, dass der Ordner "data" existiert
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)  # 🔥 Erstellt Ordner, falls er nicht existiert

    # Speichern als CSV
    csv_path = os.path.join(data_folder, f"{ticker}_data.csv")
    data.to_csv(csv_path)
    print(f"✅ Daten gespeichert unter: {csv_path}")

    return data

if __name__ == "__main__":
    df = fetch_yahoo_data("AAPL")
    print(df.head())
