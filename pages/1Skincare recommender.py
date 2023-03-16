import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time

st.set_page_config(page_icon="🧿", page_title="Skinbot")





df=pd.read_csv('csv/SKINCARE.csv')


col1, col2 = st.columns([6, 3])

with col1:
    st.image(Image.open('pictures/titulo.png'), width=600)

with col2:

    st.image(Image.open('pictures/face.jpg'), width=200)



st.subheader('Test skincare recommender')
page_names = ['Piel', 'Producto']
page = st.radio('**Elige tu tipo de piel y tus productos favoritos:** ', page_names)


if page == 'Piel' :

    Skin = st.selectbox('Selecciona tu tipo de piel', df.Skin.unique())
    st.write('¿Necesitas algún tratamiento específico?')
    result1 = st.button('Si')
    result2 = st.button('No')
    if result1:
        st.caption('Elige uno de los que te mostramos a continuación:')
        st.checkbox('Acne')
        nes_d = st.checkbox('Puntos negros')
        nes_d=st.checkbox('Poros abiertos')
        nes_d= st.checkbox('Brillos')
        st.checkbox('Cicatrices')


    elif result2:
         cont = st.button('Continuar')

else:
        

    st.markdown('**Selecciona tus productos preferidos**')

    filtro= (df[(df.Type == 'Face Cleanser') & (df.Skin == 'dry')])
    face=filtro.Products.unique()
    filtro2 = (df[(df.Type == 'Toner') & (df.Skin == 'dry')])
    toner=filtro2.Products.unique()
    filtro3= (df[(df.Type == 'Serum') & (df.Skin == 'dry')])
    serum=filtro3.Products.unique()
    filtro4=(df[(df.Type == 'Night Moisturizer') & (df.Skin == 'dry')])
    crem = filtro4.Products.unique()
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
        Prod = st.multiselect('**Serum**', serum)


    night, day, sun = st.columns(3)

    with night:
        n= st.multiselect('**Crema de noche**', crem)

    with day:
        di= st.multiselect('**Crema de día**', crema2)

    with sun:
        sd =st.multiselect('**Protector solar**',protect )


    

    

   

    with st.spinner('Analizando datos'):
        
        
            time.sleep(3)

            col1, col2 = st.columns([3, 1.75])

            with col1:
                st.success('### La recomendación de Skinbot')

                st.write('\n')
                st.write('\n')
                    
      



                st.json({'Limpiador': 'Murad - Time Release Acne Cleanser',
                'Toner': "Kiehl's - Ultra Facial Toner",
                'Serum': 'Missha - Time Revolution Prismestem100 Lifting Serum',
                'General_Moisturizer': 'Naturium Skincare - Retinol Complex Cream',
                'Day_Moisturizer': 'Isntree - Onion Newpair Gel Cream',
                'Night_Moisturizer': 'Olehenriksen - Goodnight Glow Retin-ALT Sleeping Crème',
                'Protector solar': 'IT Cosmetics - CC+ Cream with SPF 50+',
                })
                




            with col2:
                st.image(Image.open('pictures/rutina.png'), width= 350)