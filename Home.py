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
    st.image(Image.open('pictures/CARA.jpg'), width= 400)

with col2:
    st.image(Image.open('pictures/SKINBOT.png'), width=600)

with col3:
    st.write(' ')




st.title('Welcome to Skinbot')

col1, col2 = st.columns(2)

with col1:
    st.subheader('¿Qué es Skinbot?')

    st.write('Skibot es un robot creado para recomendar las mejores rutinas faciales en base a tus gustos y tus necesidades, utilizando un modelo de recomendación de machine learning, creado con una robusta base de datos.')
with col2:
     
    st.subheader('¿Cómo surge esta idea?')
    st.write('En base a las tendencias actuales y el creciente interés por mantener una piel limpia y sana, se ha realizado un modelo de machine learnign para recomendar diferentes porductos de skincare.Este modelo se puede aplicar tanto como estrategia de marketing de una empresa de cosmética, de tipo engagement, o como un chatbot implatado al inicio de la página web.')

with col1:
     
    st.subheader('¿Como se ha realizado este proyecto?')
    st.write('Este proyecto se ha realizado gracias a las herramientas aprendidas en el bootcamp de Ironhack, poniendo en práctica la extracción de datos con web scrapping, y aplicando un modelo de recomendación de machine learning en base a las valoraciones de diferentes usuarios.')


st.title('Skincare recomendations')

st.write('\n')

st.write('\n')

col1, col2 = st.columns([1,1])
with col2:
     st.write(' **1.Limpieza:** en cualquier rutina de ‘skincare’, la limpieza facial es primordial. Retira los restos de maquillaje del día con un disco de algodón empapado en agua micelar (este producto, de Kaeso, está formulado con propiedades efectivas para renovar la piel e hidratarla en profundidad). A continuación, te proponemos un gel limpiador con calor que, además de eliminar impurezas, calma y revitaliza la piel facial, dejándola suave y purificada.')
     st.write('**2. Tónico:** este es un capítulo que nos solemos saltar. Sin embargo, el tónico juega un papel fundamental en toda rutina de ‘skincare’ que se precie. El tónico ayuda a equilibrar el pH de la piel, sella los poros y prepara el cutis para recibir los productos que aplicaremos después. Además, ¡es increíblemente refrescante! No dejes de probar este elixir, cuya mezcla de menta, algodón y acerola dejará tu cutis radiante y lleno de energía.')
   
     st.write('**3. Nutrición:** antes de hidratar la piel hay que tratarla. Por ello, es de vital importancia alimentar el cutis según sus necesidades. Y los sérums se erigen, en este sentido, en las estrellas del ‘skincare’. Son concentrados de principios activos que, adicionalmente, al ser muy ligeros, penetran en la dermis fácil y rápidamente. Apuesta por uno que reponga la humedad perdida y restaure la suavidad de tu rostro.')
 
     st.write('**4. Hidratación:** independientemente de nuestro tipo de piel (seca, mixta/grasa o sensible), la crema hidratante no se debe omitir jamás en una buena rutina de ‘skincare’. Porque no solo calma la sed de la epidermis, sino que también sella los nutrientes que hemos aplicado con anterioridad. Tampoco te olvides del contorno de ojos, pues la zona ocular es la más delicada y sensible de todo el rostro. Hay que descongestionarla y revitalizarla a diario.')
 
     st.write('**5. Protección solar:** el toque final y absolutamente obligatorio en tu ritual de ‘skincare’ es una buena protección solar. Con el objetivo de levantar una barrera contra los tan nocivos rayos UV, es imperativo aplicar un protector solar, como mínimo del factor 30, aunque recomendamos siempre del 50.')





with col1: 
     st.image(Image.open('pictures/skin.jpg'), width= 370)


  


options= '¿Qué es Skinbot? ', '¿Cómo surje esta idea?', '¿Cómo se ha realizado este proyecto?'

options2= 'Github', 'Linkedin', 'E-mail'

st.sidebar.selectbox('Información sobre Skinbot', options)
if options == '¿Qué es Skinbot':
        st.subheader('¿Qué es Skinbot?')
        st.write('Skibot es un robot creado para recomendar las mejores rutinas faciales en base a tus gustos y tus necesidades, utilizando un modelo de recomendación de machine learning, creado con una robusta base de datos.')



st.sidebar.selectbox('Datos de contacto', options2)
url = 'https://github.com/cristina-apostol'




