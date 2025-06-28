import streamlit as st
import requests

st.set_page_config(page_title="☀️ Weather Report", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather Report")
st.write("")

city = st.text_input("Enter city name", placeholder="e.g. London")

if st.button("Get Weather") and city:
    try:
        # Replace with your actual FastAPI endpoint
        response = requests.get(f"http://127.0.0.1:8000/weather", params={"city": city})
        data = response.json()

        if "error" in data:
            st.error(f"Error: {data['error']}")
        else:
            st.success(f"Weather in {data['city']}")
            st.metric("Temperature (°C)", f"{data['temperature_C']} °C")
            st.write(f"🌥️ Condition: {data['weather'].capitalize()}")
    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")