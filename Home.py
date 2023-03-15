import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time

st.set_page_config(
    page_title='Skinwhat')

st.sidebar.header('Menu Lateral')
st.sidebar.subheader('Streamlit Workshop for IH')

st.sidebar.info('Aquí puedes poner una barra de navegación o zonas para cargar archivos')

upload_image = st.sidebar.file_uploader('Upload an Image', type=['png', 'jpeg', 'jpg'])
st.caption('## Imágenes')
if upload_image is not None:
    st.image(upload_image)
else:
    st.image(Image.open('src/images/ih.png'))
    