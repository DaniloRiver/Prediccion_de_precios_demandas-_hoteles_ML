import os
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

def predict_booking(data):
    return requests.post(API_URL, json=data).json()