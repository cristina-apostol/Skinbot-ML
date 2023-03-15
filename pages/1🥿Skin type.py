import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time


df=pd.read_csv('SKINCARE.csv')

col1, col2 = st.columns([3, 1])

with col1:
    st.image(Image.open('1.png'), width=500)

with col2:

    st.image(Image.open('face.jpg'), width=150)



st.subheader('Test skincare recommender 🕧')
page_names = ['Piel', 'Producto']
page = st.radio('**Elige tu tipo de piel y tus productos favoritos:** ', page_names)
st.write("**La variable devuelve X**", page)

if page == 'Piel' :
    Skin = st.selectbox('Selecciona tu tipo de piel', df.Skin.unique(), max_selections=1)
    st.write('¿Tienes algún problema añadido?')
    result1 = st.button('Si')
    result2 = st.button('No')
    if result1:
        st.write('Elige uno de los que te mostramos a continuación:')
        nes_a = st.checkbox('Acne')
        nes_d = st.checkbox('Dark Spots')
        cont = st.button('Continuar')

        if cont:
            st.write('Helo')
            st.info('Procesando tu tipo de piel ')
            progress_bar= st.progress(0)
            for perc_completed in range(100):
                time.sleep(0.009)
                progress_bar.progress(perc_completed+1)  


    elif result2:
          st.info('Procesando tu tipo de piel ')
          progress_bar= st.progress(0)
          for perc_completed in range(100):
            time.sleep(0.009)
            progress_bar.progress(perc_completed+1)  
           

else:
    st.write('##Selecciona tus productos preferidos')

filtro= (df[(df.Type == 'Face Cleanser') & (df.Skin == 'dry')])
face=filtro.Products.unique()
filtro2 = (df[(df.Type == 'Face Cleanser') & (df.Skin == 'dry')])
toner=filtro2.Products.unique()

col1, col2, col3 = st.columns(3)


with col1:

    Prod = st.multiselect('**Face Cleanser**', face)
   
with col2:
    Prod = st.multiselect('**Toner**', toner)    

