import folium
from folium.plugins import HeatMap
import pandas as pd

# Load crime dataset
df = pd.read_csv("crime_data.csv")

# Filter high-risk crime locations
high_risk_crimes = df[df["crime_type"] == 1]

# Create a map centered around crime locations
crime_map = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=6)

# Add heatmap
heat_data = list(zip(high_risk_crimes.latitude, high_risk_crimes.longitude))
HeatMap(heat_data).add_to(crime_map)

# Save the map
crime_map.save("crime_hotspots.html")