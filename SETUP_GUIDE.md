# 🚔 CrimeSpot - Setup & Run Guide

## Project Overview
**CrimeSpot** is a crime risk prediction web application that uses machine learning to predict crime hotspots based on:
- Location (latitude/longitude)
- Time of day
- Day of week
- Weather conditions
- Social media alerts
- Event density
- Previous crimes in the area

The app provides a **crime risk score (0-10)** and displays it on an interactive map.

---

## 📦 Required Libraries

### Python Libraries (Install these):
```bash
pip install streamlit pandas numpy scikit-learn xgboost joblib folium streamlit-folium fastapi uvicorn
```

---

## 🚀 How to Run the Project

### Step 1: Generate Crime Dataset
First, generate the synthetic crime data:
```bash
python crime_data.py
```
This creates `crime_data.csv` with 20,000 records.

### Step 2: Train the Machine Learning Model
Train the XGBoost model:
```bash
python model.py
```
This creates `crime_model.pkl` (the trained model file).

### Step 3: Run the Web Application
Launch the Streamlit web app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📊 How to Use the App

1. **Enter Location Details** in the sidebar:
   - Latitude (e.g., 40.7128)
   - Longitude (e.g., -74.0060)
   - Hour of the Day (0-23)
   - Day of the Week
   - Weather Condition
   - Social Media Crime Alerts (0-10)
   - Nearby Events Density (0-10)
   - Past Crimes in Area (0-10)

2. Click **"Predict Crime Risk"**

3. View the **risk level** (Low/Medium/High) and **interactive map**

---

## 🎯 For Your Interview

### Key Points to Mention:
- **Tech Stack**: Python, Streamlit, XGBoost, Scikit-learn, Folium
- **ML Model**: XGBoost Classifier with 1000 estimators
- **Features Used**: 8 features including location, temporal, and social factors
- **Dataset**: 20,000 synthetic records with realistic crime patterns
- **Accuracy**: Check the output when running `model.py`
- **Visualization**: Interactive Folium maps with risk-based markers

### Project Highlights:
✅ End-to-end ML pipeline (data generation → training → deployment)  
✅ Interactive web interface with real-time predictions  
✅ Geospatial visualization with crime risk mapping  
✅ Probability-based risk scoring (0-100%)  

---

## 📁 Project Files
- `app.py` - Main Streamlit web application
- `model.py` - ML model training script
- `crime_data.py` - Dataset generation script
- `crime_data.csv` - Generated crime dataset
- `crime_model.pkl` - Trained XGBoost model
- `api.py` - FastAPI endpoint (optional, not needed for main app)

---

## 🔧 Troubleshooting

**Error: "crime_model.pkl not found"**
→ Run `python model.py` first to train the model

**Error: "crime_data.csv not found"**
→ Run `python crime_data.py` first to generate data

**Port already in use**
→ Use: `streamlit run app.py --server.port 8502`

---

Good luck with your interview! 🚀
