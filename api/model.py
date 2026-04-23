import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "hotel_cancel_model.pkl"


def load_model():
    model = joblib.load(MODEL_PATH)
    return model