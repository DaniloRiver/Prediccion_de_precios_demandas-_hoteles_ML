# src/models/predict.py

import joblib
import pandas as pd
from pathlib import Path

# rutas robustas
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "models" / "hotel_cancel_model.pkl"


class HotelPredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        print("✅ Modelo cargado correctamente")

    def predict(self, input_data: dict):
        """
        Recibe un diccionario con datos de una reserva
        """
        df = pd.DataFrame([input_data])

        prediction = self.model.predict(df)[0]
        probability = self.model.predict_proba(df)[0][1]

        if probability > 0.7:
            risk = "ALTO"
        elif probability > 0.4:
            risk = "MEDIO"
        else:
            risk = "BAJO"

        return {
            "cancel_prediction": int(prediction),
            "cancel_probability": float(probability),
            "risk_level": risk
        }


if __name__ == "__main__":

    predictor = HotelPredictor()

    # 🔥 Ejemplo de nueva reserva
    sample_input = {
        "hotel": "City Hotel",
        "lead_time": 120,
        "arrival_date_year": 2017,
        "arrival_date_month": "July",
        "arrival_date_week_number": 27,
        "arrival_date_day_of_month": 15,
        "stays_in_weekend_nights": 2,
        "stays_in_week_nights": 3,
        "adults": 2,
        "children": 0,
        "babies": 0,
        "meal": "BB",
        "country": "PRT",
        "market_segment": "Online TA",
        "distribution_channel": "TA/TO",
        "is_repeated_guest": 0,
        "previous_cancellations": 0,
        "previous_bookings_not_canceled": 0,
        "reserved_room_type": "A",
        "assigned_room_type": "A",
        "booking_changes": 0,
        "deposit_type": "No Deposit",
        "agent": 9,
        "company": 0,
        "days_in_waiting_list": 0,
        "customer_type": "Transient",
        "adr": 100.0,
        "required_car_parking_spaces": 0,
        "total_of_special_requests": 1
    }

    result = predictor.predict(sample_input)

    print("\n🔮 Resultado de predicción:")
    print(result)