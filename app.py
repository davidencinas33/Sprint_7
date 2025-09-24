import pandas as pd
import plotly.graph_objects as go  
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
       st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

