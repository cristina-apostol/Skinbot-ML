import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time


df=pd.read_csv('SKINCARE.csv')


col1 , col2, col3 = st.columns([1 , 3, 1])
with col1:
    st.image(Image.open('CARA.jpg'), width= 100)


col2.markdown('# Qué tipo de piel tienes?')

with col2:   
    Skin = st.selectbox('Selecciona tu tipo de piel', df.Skin.unique())



col3.markdown('# Qué producto quiero?')


st.info('Procesando tu tipo de piel ')



progress_bar= st.progress(0)

for perc_completed in range(100):
    time.sleep(0.009)
    progress_bar.progress(perc_completed+1)

col2.success('Ya tenemos tu tipo de piel!')

col3.metric(label='Precio', value='12,50$', delta= 1)

with st.expander('Click to read more'):
    st.write('Heeeeeeey')