import streamlit as st
import pandas as pd
import numpy as np
import joblib  # For loading the trained model
import folium
from streamlit_folium import folium_static

# Load trained model
model = joblib.load("crime_model.pkl")  # Ensure this file exists

# App title
st.title("🚔 Crime Hotspot Predictor")

# User inputs
st.sidebar.header("Enter Location & Details")
latitude = st.sidebar.number_input("Latitude", format="%.6f")
longitude = st.sidebar.number_input("Longitude", format="%.6f")
time = st.sidebar.slider("Hour of the Day", 0, 23, 12)
day_of_week = st.sidebar.selectbox("Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
weather = st.sidebar.selectbox("Weather Condition", ["Clear", "Cloudy", "Rainy", "Stormy"])
social_media_alerts = st.sidebar.slider("Social Media Crime Alerts (0-10)", 0, 10, 2)
event_density = st.sidebar.slider("Nearby Events Density (0-10)", 0, 10, 5)
previous_crimes_nearby = st.sidebar.slider("Past Crimes in Area (0-10)", 0, 10, 3)

# Convert categorical inputs
day_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
weather_map = {"Clear": 0, "Cloudy": 1, "Rainy": 2, "Stormy": 3}

input_data = np.array([[latitude, longitude, time, day_map[day_of_week], weather_map[weather], social_media_alerts, event_density, previous_crimes_nearby]])

# Predict
if st.sidebar.button("Predict Crime Risk"):
    prediction = model.predict_proba(input_data)[0][1]  # Probability of crime
    risk_level = "🔴 High Risk" if prediction > 0.7 else "🟠 Medium Risk" if prediction > 0.4 else "🟢 Low Risk"
    
    st.subheader("🚨 Crime Risk Level")
    st.write(f"**{risk_level} ({prediction:.2%})**")

    # Map visualization
    st.subheader("📍 Crime Risk Map")
    map = folium.Map(location=[latitude, longitude], zoom_start=14)
    folium.Marker([latitude, longitude], popup=risk_level, tooltip="Location", icon=folium.Icon(color="red" if prediction > 0.7 else "orange" if prediction > 0.4 else "green")).add_to(map)
    folium_static(map)

st.write("Developed by **CrimeSpot AI**")
