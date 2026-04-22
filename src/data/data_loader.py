# src/data/data_loader.py

import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_data(self) -> pd.DataFrame:
        """
        Carga el dataset raw de hoteles
        """
        df = pd.read_csv(self.data_path)
        print(f"Dataset cargado: {df.shape}")
        return df


if __name__ == "__main__":
    loader = DataLoader("../../data/raw/hotel_bookings.csv")
    df = loader.load_data()
    print(df.head())