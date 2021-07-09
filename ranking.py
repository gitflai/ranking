import streamlit as st
import pandas as pd
import emoji

st.set_page_config(page_title = 'Ranking da 4ª Competição de ML FLAI', 
				   page_icon = 'iconeflai.png' ,
				   layout = 'centered', 
				   initial_sidebar_state = 'collapsed')

st.image('bannerflai.jpg', use_column_width = 'always')

st.markdown('# **Ranking da 4ª Competição de Machine Learning FLAI**')
st.markdown('---')

rank = pd.read_csv('4compMLflairank.csv')
subm = pd.read_csv('4compMLflai.csv')

if st.button('Clique aqui para ver o ranking geral da competição'):
	st.write(rank)

if st.button('Clique aqui para ver a listagem de todas as submissões '):
	st.write(subm)

st.markdown('---')

st.image('logoflai.png')
