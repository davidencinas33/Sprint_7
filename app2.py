import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
st.header('Análisis de datos de vehículos')
build_histogram = st.button('Construir histograma')
build_scatter = st.button('Construir diagrama de dispersión')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig_hist = px.histogram(car_data, x='odometer', title='Distribución del odómetro')
    st.plotly_chart(fig_hist)

if build_scatter:
    st.write('Construir un diagrama de dispersión de precio vs. odómetro')
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='Precio vs. Odómetro')
    st.plotly_chart(fig_scatter)


