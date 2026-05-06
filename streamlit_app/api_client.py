import os
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

def predict_booking(data):
    try:
        response = requests.post(API_URL, json=data, timeout=10)

        # 🔥 validar HTTP status
        if response.status_code != 200:
            return {
                "error": True,
                "status_code": response.status_code,
                "detail": response.text
            }

        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "error": True,
            "detail": str(e)
        }