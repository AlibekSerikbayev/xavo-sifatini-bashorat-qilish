import streamlit as st
import pandas as pd
import numpy as np
import pickle
#uzgarish 2
# Load the trained model
with open('pollution_model1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app
def main():
    st.title("Havo sifatini bashorat qilish ilovasi")

    st.write("Havo sifatini taxmin qilish uchun quyidagi ma'lumotlarni kiriting:")

    # Input fields for user data
    temperature = st.number_input("Temperatura (°C):", min_value=-30.0, max_value=50.0, value=25.0)
    humidity = st.number_input("Humidity (%):", min_value=0.0, max_value=100.0, value=60.0)
    pm25 = st.number_input("PM2.5 (µg/m³):", min_value=0.0, max_value=300.0, value=25.0)
    pm10 = st.number_input("PM10 (µg/m³):", min_value=0.0, max_value=300.0, value=40.0)
    no2 = st.number_input("NO2 (µg/m³):", min_value=0.0, max_value=200.0, value=20.0)
    so2 = st.number_input("SO2 (µg/m³):", min_value=0.0, max_value=100.0, value=15.0)
    co = st.number_input("CO (mg/m³):", min_value=0.0, max_value=10.0, value=0.9)
    proximity = st.number_input("Sanoat hududlariga yaqinlik(km):", min_value=0.0, max_value=50.0, value=5.0)
    population_density = st.number_input("Aholi zichligi (odam/km²):", min_value=200, max_value=500, value=300, step=1)

    # Predict button
    if st.button("Xavo sifatini aniqlash"):
        # Create input data for the model
        input_data = np.array([[
            temperature, humidity, pm25, pm10, no2, so2, co, proximity, population_density
        ]])

        # Make prediction
        prediction = model.predict(input_data)

        # Display the result
        st.write("### Bashorat qilingan havo sifati:", prediction[0])

if __name__ == "__main__":
    main()


