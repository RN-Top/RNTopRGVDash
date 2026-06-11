import streamlit as st
import pandas as pd

st.title("🌵 RGV Dash")
st.subheader("Delivery Time Predictor")

distance = st.slider("Distance (miles)", 0.5, 10.0, 3.0)
time_of_day = st.slider("Time of day", 6, 23, 13)
rush_hour = st.checkbox("Is it rush hour?")

if st.button("Predict Delivery Time"):
    input_data = pd.DataFrame({
        'distance_miles': [distance],
        'time_of_day': [time_of_day],
        'is_peak': [rush_hour] })
#simulated learning mode
    simulated_time = 15 + (distance * 4) +(12 if rush_hour else 0)

    
    st.success(f"🍔 Your food will arrive in about **{int(simulated_time)}** minutes")
