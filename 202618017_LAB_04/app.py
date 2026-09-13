import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="NYC Airbnb Price Predictor", page_icon="🗽", layout="centered")

st.title("🗽 NYC Airbnb Nightly Price Predictor")
st.write("Estimate the optimal nightly price for an NYC listing.")

@st.cache_resource
def load_pipeline():
    return joblib.load("airbnb_model.pkl")

pipeline = load_pipeline()

# Borough center coordinates mapping (eliminates forced coordinate input)
BOROUGH_COORDS = {
    "Manhattan": (40.7831, -73.9712),
    "Brooklyn": (40.6782, -73.9442),
    "Queens": (40.7282, -73.7949),
    "Bronx": (40.8448, -73.8648),
    "Staten Island": (40.5795, -74.1502)
}

st.subheader("Listing Information")
col1, col2 = st.columns(2)

with col1:
    neighbourhood_group = st.selectbox("Borough", list(BOROUGH_COORDS.keys()))
    room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])

with col2:
    minimum_nights = st.number_input("Minimum Stay (Nights)", min_value=1, max_value=365, value=2)
    availability_365 = st.slider("Days Available per Year", 0, 365, value=180)

# Default location set based on selected borough
default_lat, default_lon = BOROUGH_COORDS[neighbourhood_group]

# Technical and historical metrics hidden in an collapsible expander
with st.expander("⚙️ Advanced Settings & Coordinates (Optional)"):
    st.caption("Adjust exact GPS coordinates or historical host metrics if available.")
    col_adv1, col_adv2 = st.columns(2)
    with col_adv1:
        latitude = st.number_input("Latitude", value=default_lat, format="%.4f")
        longitude = st.number_input("Longitude", value=default_lon, format="%.4f")
        calculated_host_listings_count = st.number_input("Host Total Listings Count", min_value=1, value=1)
    with col_adv2:
        number_of_reviews = st.number_input("Total Historical Reviews", min_value=0, value=0)
        reviews_per_month = st.number_input("Reviews per Month", min_value=0.0, value=0.0, format="%.2f")

if st.button("Predict Price", type="primary"):
    # Compute distance to Midtown Manhattan dynamically
    dist_to_midtown = np.sqrt((latitude - 40.7580)**2 + (longitude - (-73.9855))**2)
    
    # Input DataFrame matching model schema
    input_df = pd.DataFrame([{
        "latitude": latitude,
        "longitude": longitude,
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "reviews_per_month": reviews_per_month,
        "calculated_host_listings_count": calculated_host_listings_count,
        "availability_365": availability_365,
        "dist_to_midtown": dist_to_midtown,
        "neighbourhood_group": neighbourhood_group,
        "room_type": room_type
    }])
    
    pred_log = pipeline.predict(input_df)[0]
    pred_price = np.expm1(pred_log)
    
    st.success(f"### Estimated Price: **${pred_price:.2f}** / night")
