from fastapi import FastAPI
import pandas as pd

from api.model import load_model
from api.schemas import BookingInput

app = FastAPI(
    title="Hotel Cancellation Prediction API",
    version="1.0"
)

# 🔥 cargar modelo UNA sola vez
model = load_model()


@app.get("/")
def home():
    return {"message": "API de predicción de cancelación de hoteles 🚀"}


@app.post("/predict")
def predict(data: BookingInput):

    # convertir input a dataframe
    df = pd.DataFrame([data.dict()])

    # predicción
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

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