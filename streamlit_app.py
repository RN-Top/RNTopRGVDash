import streamlit as st
import pandas as pd
import joblib
# Load the model
model = joblib.load('rgv_model.pkl')

st.title("🌵 RGV Dash")
st.subheader("Delivery Time Predictor")

distance = st.slider("Distance (miles)", 0.5, 10.0, 3.0)
time_of_day = st.slider("Time of day", 6, 23, 13)
rush_hour = st.checkbox("Is it rush hour?")

if st.button("Predict Delivery Time"):
    input_data = pd.DataFrame({
        'distance_miles': ,
        'time_of_day': ,
        'is_peak': })
    
    prediction = model.predict(input_data)[0]
    st.success(f"🍔 Your food will arrive in about **{int(prediction)} minutes**")
