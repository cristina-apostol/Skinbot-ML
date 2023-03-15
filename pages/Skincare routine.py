
import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time
import pandas as pd
import numpy as np

from scipy.spatial.distance import pdist, squareform

st.set_page_config(page_icon="🧿", page_title="Skinbot", layout="wide")


st.subheader('¿Qué productos existen según tu tipo de piel?')



df=pd.read_csv('SKINCARE.csv')
    
col1 , col2 = st.columns(2)

with col1:   
    Skin = st.selectbox('Selecciona tu tipo de piel', df.Skin.unique())

with col2:
    Type = st.selectbox ('Selecciona un tipo de porducto', df.Type.unique())


filtro = (df[(df.Type == Type) & (df.Skin == Skin)])
serum= filtro[['Type', 'Products', 'Skin']]
st.dataframe(serum)


st.subheader('Meter aqui las graficas')