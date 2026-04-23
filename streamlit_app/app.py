import streamlit as st
from api_client import predict_booking

st.set_page_config(page_title="Hotel ML Predictor", layout="centered")

st.title("🏨 Hotel Cancellation Predictor")

st.write("Ingresa los datos de la reserva para predecir cancelación")

# Inputs básicos (puedes expandir luego)
lead_time = st.number_input("Lead Time", 0, 500, 100)
adults = st.number_input("Adults", 1, 10, 2)
children = st.number_input("Children", 0, 5, 0)
babies = st.number_input("Babies", 0, 3, 0)
adr = st.number_input("ADR (Average Daily Rate)", 0.0, 1000.0, 100.0)

if st.button("Predecir Cancelación 🚀"):

    payload = {
        "lead_time": lead_time,
        "adults": adults,
        "children": children,
        "babies": babies,
        "adr": adr,

        # valores dummy (ajustar según tu API real)
        "hotel": "City Hotel",
        "arrival_date_year": 2017,
        "arrival_date_month": "July",
        "arrival_date_week_number": 30,
        "arrival_date_day_of_month": 15,
        "stays_in_weekend_nights": 2,
        "stays_in_week_nights": 3,
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
        "required_car_parking_spaces": 0,
        "total_of_special_requests": 1
    }

    result = predict_booking(payload)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Resultado obtenido 🚀")

        st.metric("Cancelación (0/1)", result["cancel_prediction"])
        st.metric("Probabilidad", round(result["cancel_probability"], 3))