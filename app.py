import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Air Quality Monitoring Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Air Quality Monitoring Dashboard")
st.write("Monitor and understand air pollution levels")

st.sidebar.header("Enter Air Quality Data")

city = st.sidebar.text_input("City Name", "Nellore")
aqi = st.sidebar.slider("Air Quality Index (AQI)", 0, 500, 100)
pm25 = st.sidebar.number_input("PM2.5", min_value=0.0, value=35.0)
pm10 = st.sidebar.number_input("PM10", min_value=0.0, value=60.0)
temperature = st.sidebar.number_input("Temperature (°C)", value=30.0)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 60)

if aqi <= 50:
    level = "Good"
elif aqi <= 100:
    level = "Satisfactory"
elif aqi <= 200:
    level = "Moderate"
elif aqi <= 300:
    level = "Poor"
elif aqi <= 400:
    level = "Very Poor"
else:
    level = "Severe"

st.subheader(f"Air Quality Report: {city}")

col1, col2, col3, col4 = st.columns(4)

col1.metric("AQI", aqi)
col2.metric("PM2.5", f"{pm25} µg/m³")
col3.metric("PM10", f"{pm10} µg/m³")
col4.metric("Temperature", f"{temperature} °C")

st.info(f"Current pollution category: {level}")

st.subheader("Air Quality Data Visualization")

data = pd.DataFrame({
    "Pollutant": ["PM2.5", "PM10"],
    "Value": [pm25, pm10]
})

fig = px.bar(
    data,
    x="Pollutant",
    y="Value",
    color="Pollutant",
    title="Pollutant Concentration"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Environmental Information")
st.write(f"City: {city}")
st.write(f"Humidity: {humidity}%")
st.write(f"Air Quality Category: {level}")

st.success("Air Quality Dashboard is running!")