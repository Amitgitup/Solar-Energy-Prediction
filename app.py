import streamlit as st
import numpy as np
import pandas as pd 
import pickle

## Loading the pickle file
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('model1.pkl', 'rb') as file:
    model = pickle.load(file)

## Streamlit app
st.title("Solar Energy Prediction")

## User Input
temperature_2_m_above_gnd = st.slider("Temperature", 5.35, 36.0)   ## 35.5
relative_humidity_2_m_above_gnd = st.slider("Humidity", 7.0, 100.0)
mean_sea_level_pressure_MSL = st.slider("Mean Sea Pressure", 998.0, 1045.0)
total_precipitation_sfc = st.slider("Precipitation", 0.0, 4.0)
snowfall_amount_sfc = st.slider("Snowfall", 0.0, 2.0)
total_cloud_cover_sfc = st.slider("Total Cloud Cover", 0.0, 100.0)   ## [0.0, 25.0]
high_cloud_cover_high_cld_lay = st.slider("High Cloud Cover", 0.0, 100.0)  ## 
medium_cloud_cover_mid_cld_lay = st.slider("Medium Cloud Cover", 0.0, 100.0)
low_cloud_cover_low_cld_lay = st.slider("Low Cloud Cover", 0.0, 100.0)
shortwave_radiation_backwards_sfc = st.selectbox("Shorwave  Radiation", [0.0, 950.0])
wind_speed_10_m_above_gnd = st.slider("Wind Speed 10m above ground", 0.0, 42.0)
wind_direction_10_m_above_gnd = st.slider("Wind Direction 10m above ground", 1.0, 360.00)
angle_of_incidence = st.slider("Angle of Incidence", 5.0, 115.0)
zenith = st.slider("Zenith", 18.0, 115.0)
azimuth = st.slider("Azimuth", 55.0, 285.0)


## Prepare the Input data
input_data = pd.DataFrame({
    'temperature_2_m_above_gnd': [temperature_2_m_above_gnd],
    'relative_humidity_2_m_above_gnd': [relative_humidity_2_m_above_gnd],
    'mean_sea_level_pressure_MSL': [mean_sea_level_pressure_MSL],
    'total_precipitation_sfc': [total_precipitation_sfc],
    'snowfall_amount_sfc': [snowfall_amount_sfc],
    'total_cloud_cover_sfc': [total_cloud_cover_sfc],
    'high_cloud_cover_high_cld_lay': [high_cloud_cover_high_cld_lay],
    'medium_cloud_cover_mid_cld_lay': [medium_cloud_cover_mid_cld_lay],
    'low_cloud_cover_low_cld_lay': [low_cloud_cover_low_cld_lay],
    'shortwave_radiation_backwards_sfc': [shortwave_radiation_backwards_sfc],
    'wind_speed_10_m_above_gnd': [wind_speed_10_m_above_gnd],
    'wind_direction_10_m_above_gnd': [wind_direction_10_m_above_gnd],
    'angle_of_incidence': [angle_of_incidence],
    'zenith': [zenith],
    'azimuth': [azimuth]
})

## Scale the input data
input_data_scaled = scaler.transform(input_data)

## Predict the Estimated Solar Energy (KW)
prediction = model.predict(input_data_scaled)
predicted_power = prediction[0]

st.write(f'Predicted Solary Generation: {predicted_power:.3f}')