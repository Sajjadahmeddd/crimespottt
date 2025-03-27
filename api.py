from fastapi import FastAPI
import joblib
import pandas as pd

# Load trained model
model = joblib.load("crime_model.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to CrimeSpot API!"}

@app.post("/predict/")
def predict_crime(latitude: float, longitude: float, time: int, day_of_week: int, weather: int, social_media_alerts: int, event_density: int, previous_crimes_nearby: int):
    data = pd.DataFrame([[latitude, longitude, time, day_of_week, weather, social_media_alerts, event_density, previous_crimes_nearby]], 
                        columns=["latitude", "longitude", "time", "day_of_week", "weather", "social_media_alerts", "event_density", "previous_crimes_nearby"])
    prediction = model.predict(data)[0]
    return {"crime_risk": "High" if prediction == 1 else "Low"}
