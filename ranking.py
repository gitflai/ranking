import streamlit as st
import pandas as pd
import emoji 
import st_aggrid as stg 


st.set_page_config(page_title = '9ª Competição de ML FLAI', 
				   page_icon = 'iconeflai.png' ,
				   layout = 'centered', 
				   initial_sidebar_state = 'collapsed')
 
  
st.image('bannerflai.jpg', use_column_width = 'always')


st.markdown('''
	# Ranking da 9ª Competição de Machine Learning FLAI 

	###### NOVA Deadline: 26/06/2022 às 20h!
	---
''')

rank = pd.read_csv('4compMLflairank.csv')
subm = pd.read_csv('4compMLflai.csv')
liga = pd.read_csv('liga.csv') 

#rank.index = rank['Nome']
#rank.drop(['Nome'], axis = 1, inplace = True)

#st.markdown('Em manutenção... :poop:')

col1, col2, col3 = st.beta_columns(3) 

if col1.button('RANKING GERAL DA COMPETIÇÃO'):
	st.markdown('---') 
	st.write(rank.to_html(index=False), unsafe_allow_html=True)

if col2.button('LISTAGEM DE TODAS AS SUBMISSÕES'):
	st.markdown('---') 
	stg.AgGrid(subm.round(5), height = 800, fit_columns_on_grid_load = True)
	
if col3.button('PONTOS NA LIGA'):
	st.markdown('---') 
	st.subheader('Resultado provisório, baseado na situação atual da competição vigente')
	st.write(liga.to_html(index=False), unsafe_allow_html=True)

st.markdown('---') 

st.sidebar.image('logoflai.png')
st.sidebar.markdown('---')
st.sidebar.markdown('#### Versão 0.1.0')
