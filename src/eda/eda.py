# src/eda/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EDA:
    def __init__(self, df):
        self.df = df

    def cancellation_rate(self):
        plt.figure()
        sns.countplot(x="is_canceled", data=self.df)
        plt.title("Cancelaciones de reservas")
        plt.show()

    def lead_time_distribution(self):
        plt.figure()
        sns.histplot(self.df["lead_time"], bins=50)
        plt.title("Distribución de Lead Time")
        plt.show()

    def adr_by_hotel(self):
        plt.figure()
        sns.boxplot(x="hotel", y="adr", data=self.df)
        plt.title("Precio promedio por tipo de hotel")
        plt.show()

    def run(self):
        self.cancellation_rate()
        self.lead_time_distribution()
        self.adr_by_hotel()


if __name__ == "__main__":
    df = pd.read_csv("../../data/raw/hotel_bookings.csv")

    eda = EDA(df)
    eda.run()