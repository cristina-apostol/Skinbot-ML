
import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time
import numpy as np
import altair as alt
import plotly.express as px

from scipy.spatial.distance import pdist, squareform


st.set_page_config(page_icon="🧿", page_title="Skinbot", layout="wide")


st.subheader('Filtro productos según tipo de piel y ranking.')


df = pd.read_csv('csv/skincaret.csv')
    
col1 , col2 = st.columns(2)

with col1:   
    Skin = st.selectbox('Selecciona tu tipo de piel', df.Skin.unique())

with col2:
    Type = st.selectbox ('Selecciona un tipo de porducto', df.Type.unique())



col1, col2, col3 = st.columns([1,8,1])
col1 = " "

with col2:

    filtro = (df[(df.Type == Type) & (df.Skin == Skin)])
    rev= filtro.sort_values(by= 'Reviews', ascending = False)
    st.dataframe(rev)

col3= " "



st.subheader('Análisis mejores marcas')
df = pd.read_csv('csv/skincare2.csv')
filtro= df.Brand.unique()



brand_counts = df['Brand'].value_counts().reset_index()
brand_counts.columns = ['Brand', 'Count']

# Creamos un gráfico de barras utilizando Plotly Express
fig = px.bar(brand_counts, x='Brand', y='Count', color='Brand')

# Utilizamos Streamlit para mostrar el gráfico
st.plotly_chart(fig)
