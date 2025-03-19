import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_touohxv0.json")

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Title
st.title("🔄 Stylish Unit Converter")

# Display animation
if lottie_animation:
    st_lottie(lottie_animation, height=150, key="convert")

# Conversion categories
categories = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371, "Yard": 1.09361},
    "Temperature": {"Celsius": 1, "Fahrenheit": 1.8, "Kelvin": 1},
    "Weight": {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462},
    "Speed": {"Meter/Second": 1, "Kilometer/Hour": 3.6, "Miles/Hour": 2.23694},
    "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600},
    "Area": {"Square Meter": 1, "Square Kilometer": 0.000001, "Acre": 0.000247105},
    "Volume": {"Cubic Meter": 1, "Liter": 1000, "Gallon": 264.172},
    "Pressure": {"Pascal": 1, "Bar": 0.00001, "PSI": 0.000145038},
    "Energy": {"Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006},
    "Data Storage": {"Byte": 1, "Kilobyte": 0.001, "Megabyte": 0.000001}
}

# Select category
category = st.selectbox("Select Conversion Type", list(categories.keys()))

# Select units
units = list(categories[category].keys())
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Input value
value = st.number_input("Enter value", min_value=0.0, format="%.4f")

# Conversion logic
def convert(value, from_unit, to_unit, conversion_dict):
    base_value = value / conversion_dict[from_unit]  # Convert to base unit
    return base_value * conversion_dict[to_unit]  # Convert to target unit

# Perform conversion if valid
if st.button("Convert 🔄"):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 1.8) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) / 1.8
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        else:
            result = value  # Same unit
    else:
        result = convert(value, from_unit, to_unit, categories[category])
    
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
