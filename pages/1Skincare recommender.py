import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time


df=pd.read_csv('SKINCARE.csv')

col1, col2 = st.columns([6, 4])

with col1:
    st.image(Image.open('titulo.png'), width=600)

with col2:

    st.image(Image.open('face.jpg'), width=200)



st.subheader('Test skincare recommender 🕧')
page_names = ['Piel', 'Producto']
page = st.radio('**Elige tu tipo de piel y tus productos favoritos:** ', page_names)
st.write("**La variable devuelve X**", page)

if page == 'Piel' :
    Skin = st.selectbox('Selecciona tu tipo de piel', df.Skin.unique())
    st.write('¿Tienes algún problema añadido?')
    result1 = st.button('Si')
    result2 = st.button('No')
    if result1:
        st.write('Elige uno de los que te mostramos a continuación:')
        nes_a = st.checkbox('Acne')
        nes_d = st.checkbox('Puntos negros')
        nes_d=st.checkbox('Poros abierto')
        nes_d= st.checkbox('Brillos')
        cont = st.button('Continuar')

        if cont:
            st.write('Helo')
            st.info('Procesando tu tipo de piel ')
            progress_bar= st.progress(0)
            for perc_completed in range(100):
                time.sleep(0.009)
                progress_bar.progress(perc_completed+1)  


    elif result2:
          st.info('Elige tus productos favoritos mientras procesamos tu piel')
          progress_bar= st.progress(0)
          for perc_completed in range(100):
            time.sleep(0.15)
            progress_bar.progress(perc_completed+1)  
           

else:
    st.write('##Selecciona tus productos preferidos')

    filtro= (df[(df.Type == 'Face Cleanser') & (df.Skin == 'dry')])
    face=filtro.Products.unique()
    filtro2 = (df[(df.Type == 'Toner') & (df.Skin == 'dry')])
    toner=filtro2.Products.unique()
    filtro3= (df[(df.Type == 'Serum') & (df.Skin == 'dry')])
    serum=filtro3.Products.unique()
    filtro4=(df[(df.Type == 'Night Moisturizer') & (df.Skin == 'dry')])
    crema = filtro4.Products.unique()
    filtro5= (df[(df.Type == 'Day Moisturizer') & (df.Skin == 'dry')])
    crema2=filtro5.Products.unique()
    filtro6 = (df[(df.Type == 'Sunscreen') & (df.Skin == 'dry')])
    protect= filtro6.Products.unique()

    col1, col2, col3 = st.columns(3)


    with col1:

        Prod = st.multiselect('**Limpiador**', face)
    
    with col2:
        Prod = st.multiselect('**Toner**', toner) 

    with col3:
        st.multiselect('**Serum**', serum)


col1, col2, col3 = st.columns(3)

with col1:

    st.multiselect('**Crema de noche**', crema)

with col2:
    st.multiselect('**Crema de día**', crema2)

with col3:
    st.multiselect('**Protector solar**',protect )



       

