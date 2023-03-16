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




st.title('Bienvenido a Skinbot')

st.subheader('¿Qué es Skinbot?')

st.write('Skibot es un robot creado para recomendar las mejores rutinas faciales en base a tus gustos y tus necesidades, utilizando un modelo de recomendación de machine learning, creado con una robusta base de datos.')

st.subheader('¿Cómo surge esta idea?')
st.write('En base a las tendencias actuales y el creciente interés por mantener una piel limpia y sana, s')

st.sidebar.header('Bootcamp análisis de datos Ironhack')
st.sidebar.subheader('Proyecto modelo de recomendación')



st.sidebar.button('Click aquí si deseas ver más información')

st.sidebar.info('By Cristina Apostol')