import pandas as pd
import numpy as np

# ✅ Generate More Data
num_records = 20000  # Increased to 20,000

np.random.seed(42)

data = {
    "latitude": np.random.uniform(10.0, 50.0, num_records),
    "longitude": np.random.uniform(-120.0, -70.0, num_records),
    "time": np.random.randint(0, 24, num_records),  # 0 to 23 hours
    "day_of_week": np.random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], num_records),
    "weather": np.random.choice(["Clear", "Rainy", "Stormy", "Foggy"], num_records),
    "social_media_alerts": np.random.randint(0, 10, num_records),
    "event_density": np.random.randint(0, 5, num_records),
    "previous_crimes_nearby": np.random.randint(0, 20, num_records),
}

df = pd.DataFrame(data)

# ✅ Introduce Realistic Crime Patterns
df["crime_risk_score"] = (
    0.4 * (df["time"] >= 20)  # Higher crime risk at night
    + 0.3 * (df["event_density"] >= 3)  # High event density attracts crime
    + 0.2 * (df["social_media_alerts"] >= 5)  # Social media alerts indicate crime
    + 0.2 * (df["previous_crimes_nearby"] >= 10)  # Areas with prior crimes are risky
)

df["crime_type"] = np.where(df["crime_risk_score"] > 0.5, 1, 0)  # 1 = High crime risk, 0 = Low risk

# ✅ Save dataset
df.to_csv("crime_data.csv", index=False)
print("✅ New dataset generated with more meaningful crime patterns.")
