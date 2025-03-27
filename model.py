import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import joblib

# ✅ Load dataset
df = pd.read_csv("crime_data.csv")

# ✅ Encode categorical features
df["day_of_week"] = df["day_of_week"].astype("category").cat.codes
df["weather"] = df["weather"].astype("category").cat.codes

# ✅ Feature Selection (Focusing on Stronger Features)
X = df[["latitude", "longitude", "time", "day_of_week", "weather", "social_media_alerts", "event_density", "previous_crimes_nearby"]]
y = df["crime_type"]

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# ✅ Train XGBoost with Optimized Settings
model = XGBClassifier(n_estimators=1000, learning_rate=0.03, max_depth=10, colsample_bytree=0.9, subsample=0.9, random_state=42)
model.fit(X_train, y_train)

# ✅ Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"🔥 Model Accuracy: {accuracy:.3f}")

# ✅ Save model
joblib.dump(model, "crime_model.pkl")
