import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time


df=pd.read_csv('SKINCARE.csv')


col1, col2 = st.columns ([3,1])

col1.markdown('# Skincare recommender')

with col2:
     st.image(Image.open('CARA.jpg'), width= 150)

col1 , col2, col3 = st.columns([1 , 4, 1])
col1: " "
    

col2.markdown('# ¿Cuál es tu tipo de piel?')

with col3:
    st.image(Image.open('CARA.jpg'), width= 100)



page_names = ['Piel', 'Producto']
page = st.radio('Navegador', page_names)
st.write("**La variable devuelve X**", page)

if page == 'Piel' :
    Skin = st.multiselect('Selecciona tu tipo de piel', df.Skin.unique(), max_selections=1)
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
    st.subheader('Hola boton')
    st.write('hey')
    result = st.button('Hz click')
    st.write ('Bien', result)

    if result :
        nes_c= st.checkbox ('NO SE Q HACE')
        if nes_c:
            st.write('Algo pasa')









col1 , col2, col3 = st.columns([1 , 3, 1])
with col1:
    st.image(Image.open('CARA.jpg'), width= 100)


col2.markdown('# Qué tipo de piel tienes?')

with col2:   
    Skin = st.multiselect('Selecciona tu tipo de piel', df.Skin.unique(), max_selections=3)


with col3: " "


#st.info('Procesando tu tipo de piel ')



progress_bar= st.progress(0)

#for perc_completed in range(100):
    #time.sleep(0.009)
    #progress_bar.progress(perc_completed+1)

col2.success('Ya tenemos tu tipo de piel!')

col3.metric(label='Precio', value='12,50$', delta= 1)

with st.expander('Click to read more'):
    st.write('Heeeeeeey')