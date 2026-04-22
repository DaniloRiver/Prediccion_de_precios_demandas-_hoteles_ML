# src/data/data_preprocessing.py

import pandas as pd
import numpy as np
from pathlib import Path


class DataPreprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def handle_missing_values(self):
        """
        Manejo de valores nulos
        """
        self.df["children"] = self.df["children"].fillna(0)
        self.df["country"] = self.df["country"].fillna("Unknown")
        self.df["agent"] = self.df["agent"].fillna(0)
        self.df["company"] = self.df["company"].fillna(0)

        return self.df

    def feature_engineering(self):
        """
        Creación de nuevas variables
        """
        self.df["total_nights"] = (
            self.df["stays_in_week_nights"] +
            self.df["stays_in_weekend_nights"]
        )

        self.df["is_family"] = np.where(
            (self.df["children"] > 0) | (self.df["babies"] > 0),
            1,
            0
        )

        self.df["booking_lead_time"] = self.df["lead_time"]

        return self.df

    def encode_categorical(self):
        """
        Encoding básico (baseline)
        """
        categorical_cols = [
            "hotel",
            "arrival_date_month",
            "meal",
            "country",
            "market_segment",
            "distribution_channel",
            "deposit_type",
            "customer_type"
        ]

        self.df = pd.get_dummies(self.df, columns=categorical_cols, drop_first=True)

        return self.df

    def run_pipeline(self):
        self.handle_missing_values()
        self.feature_engineering()
        self.encode_categorical()

        print("Preprocesamiento completado:", self.df.shape)
        return self.df


if __name__ == "__main__":

    # Ruta base del proyecto
    BASE_DIR = Path(__file__).resolve().parents[2]

    # Ruta al dataset
    data_path = BASE_DIR / "data" / "raw" / "hotel_bookings.csv"

    df = pd.read_csv(data_path)

    preprocessor = DataPreprocessor(df)
    df_processed = preprocessor.run_pipeline()

    output_path = BASE_DIR / "data" / "processed" / "hotel_bookings_processed.csv"
    df_processed.to_csv(output_path, index=False)