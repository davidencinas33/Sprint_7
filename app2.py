import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos desde el archivo CSV
car_data = pd.read_csv('../vehicles_us.csv')

# Título de la aplicación
st.header('Análisis de datos de vehículos')

# Crear las casillas de verificación
build_histogram = st.checkbox('Construir un histograma para el odómetro')
build_scatter = st.checkbox('Construir un diagrama de dispersión de precio vs. odómetro')

if build_histogram:
    # Si la casilla del histograma está seleccionada, construirlo
    fig_hist = px.histogram(car_data, x='odometer', title='Distribución del odómetro')
    st.plotly_chart(fig_hist)

if build_scatter:
    # Si la casilla del diagrama de dispersión está seleccionada, construirlo
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='Precio vs. Odómetro')
    st.plotly_chart(fig_scatter)
