import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("flood_model.pkl", "rb"))

st.title("🌊 Flood Prediction App")

topography = st.number_input("Topography & Drainage Score", 0, 10, 5)
dams = st.number_input("Dams Quality Score", 0, 10, 5)
political = st.number_input("Political Factors Score", 0, 10, 5)
preparedness = st.number_input("Disaster Preparedness Score", 0, 10, 5)
population = st.number_input("Population Score", 0, 10, 5)

if st.button("Predict Flood Probability"):
    features = [[topography, dams, political, preparedness, population]]
    prediction = model.predict(features)[0]
    st.success(f"Predicted Flood Probability: {prediction:.2f}")
