import pickle
import streamlit as st
import pandas as pd
import numpy as np
import os
import altair as alt

# Load model
model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

st.title('Prediksi Harga Mobil')

# Dataset Section
st.header("Dataset")
# Load dataset
df1 = pd.read_csv('CarPrice.csv')
st.dataframe(df1)

# Visualisasi Grafik
st.write("Grafik Highway-mpg")
chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
st.line_chart(chart_highwaympg)

st.write("Grafik curbweight")
chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
st.line_chart(chart_curbweight)

st.write("Grafik horsepower")
chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
st.line_chart(chart_horsepower)

# Input nilai dari variable independent
highwaympg = st.number_input('Highway MPG', min_value=0.0, max_value=100.0, value=25.0)
curbweight = st.number_input('Curb Weight', min_value=0, max_value=5000, value=2500)
horsepower = st.number_input('Horsepower', min_value=0, max_value=500, value=150)

if st.button("Prediksi"):
    # Prediksi variable yang telah diinputkan
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

    # Convert ke string
    harga_mobil_str = np.array(car_prediction)
    harga_mobil_float = float(harga_mobil_str[0])
    
    # Tampilkan hasil prediksi
    harga_mobil_formatted = f"${harga_mobil_float:,.2f}"
    st.write("Harga mobil yang diprediksi:", harga_mobil_formatted)
