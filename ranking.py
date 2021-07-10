import streamlit as st
import pandas as pd
import emoji 
 

st.set_page_config(page_title = 'Ranking da 4ª Competição de ML FLAI', 
				   page_icon = 'iconeflai.png' ,
				   layout = 'centered', 
				   initial_sidebar_state = 'collapsed')
 


st.image('bannerflai.jpg', use_column_width = 'always')

st.markdown('# **Ranking da 4ª Competição de Machine Learning FLAI**')
 
st.write('*Última Atualização: 09/07/2021 - 21h00')
st.markdown('---')

rank = pd.read_csv('4compMLflairank.csv')
subm = pd.read_csv('4compMLflai.csv')

rank.index = rank['Nome']
rank.drop(['Nome'], axis = 1, inplace = True)

col1, col2 = st.beta_columns(2) 

if col1.button('Clique aqui para ver o ranking geral da competição'):
	st.table(rank)

if col2.button('Clique aqui para ver a listagem de todas as submissões '):
	st.write(subm)

st.markdown('---') 

st.image('logoflai.png')
