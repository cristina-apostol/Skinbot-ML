import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time

st.set_page_config(page_icon="🧿", page_title="Skinbot", layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(Image.open('CARA.jpg'), width= 400)

with col2:
    st.image(Image.open('SKINBOT.png'), width=600)

with col3:
    st.write(' ')




st.title('Welcome to Skinbot')

st.subheader('¿Qué es Skinbot?')

st.write('Skibot es un robot creado para recomendar las mejores rutinas faciales en base a tus gustos y tus necesidades, utilizando un modelo de recomendación de machine learning, creado con una robusta base de datos.')

st.subheader('¿Cómo surge esta idea?')
st.write('En base a las tendencias actuales y el creciente interés por mantener una piel limpia y sana, se ha realizado un modelo de machine learnign para recomendar diferentes porductos de skincare.Este modelo se puede aplicar tanto como estrategia de marketing de una empresa de cosmética, de tipo engagement, o como un chatbot implatado al inicio de la página web.')

st.subheader('¿Como se ha realizado este proyecto?')
st.write('Este proyecto se ha realizado gracias a las herramientas aprendidas en el bootcamp de Ironhack, poniendo en práctica la extracción de datos con web scrapping, y aplicando un modelo de recomendación de machine learning en base a las valoraciones de diferentes usuarios.')

st.sidebar.header('Modelo de recomendación con machine learning')
st.sidebar.subheader('Proyecto Data analysis | Ironhack')


url = 'https://github.com/cristina-apostol'

if st.sidebar.button('Github: Cristina Apostol'):
     webbrowser.open_new_tab(url)
