from fastapi import FastAPI
import pandas as pd
import traceback

from api.model import load_model
from api.schemas import BookingInput

app = FastAPI(
    title="Hotel Cancellation Prediction API",
    version="1.0"
)

model = None


@app.on_event("startup")
def startup():
    global model
    try:
        print("🚀 Loading model...")
        model = load_model()
        print("✅ Model loaded successfully")
    except Exception as e:
        print("❌ ERROR LOADING MODEL")
        print(traceback.format_exc())
        raise e


@app.get("/")
def home():
    return {"message": "API de predicción de cancelación de hoteles 🚀"}


@app.post("/predict")
def predict(data: BookingInput):

    df = pd.DataFrame([data.dict()])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    risk = (
        "ALTO" if probability > 0.7 else
        "MEDIO" if probability > 0.4 else
        "BAJO"
    )

    return {
        "cancel_prediction": int(prediction),
        "cancel_probability": float(probability),
        "risk_level": risk
    }