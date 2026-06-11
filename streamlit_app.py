import streamlit as st
import pandas as pd
import joblib

st.title("🌵 RGV Dash")
st.subheader("Delivery Time Predictor")

#load real pickle model back in 
model = joblib.load('rgv_model.pkl')

distance = st.slider("Distance (miles)", 0.5, 10.0, 3.0)
time_of_day = st.slider("Time of day", 6, 23, 13)
rush_hour = st.checkbox("Is it rush hour?")

if st.button("Predict Delivery Time"):
    input_data = pd.DataFrame({
        'distance_miles': [distance],
        'time_of_day': [time_of_day],
        'is_peak': [rush_hour] })

   # use your real machine learning to predict
    prediction = model.predict(input_data)[0]
    st.success(f"🍔 Your food will arrive in about **{int(prediction)}** minutes")
