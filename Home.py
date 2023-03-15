import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import time

st.set_page_config(
    page_title='Skinwhat')

st.title('¿Qué tipo de piel tengo?'':panda_face:')



col1 , col2, col3 = st.columns([2 , 2, 2])

col1.markdown("# Bienvenidos a skinwhat")
col2.markdown('# Qué tipo de piel tengo?')
col3.markdown('# Qué producto quiero?')
col2.info('Procesando tu tipo de piel ')
progress_bar= col2.progress(0)

for perc_completed in range(100):
    time.sleep(0.009)
    progress_bar.progress(perc_completed+1)

col2.success('Ya tenemos tu tipo de piel!')

col3.metric(label='Precio', value='12,50$', delta= 1)

with st.expander('Click to read more'):
    st.write('Heeeeeeey')

    