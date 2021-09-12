import streamlit as st
import pandas as pd
import emoji 
import st_aggrid as stg 


st.set_page_config(page_title = 'Ranking da 5ª Competição de ML FLAI', 
				   page_icon = 'iconeflai.png' ,
				   layout = 'centered', 
				   initial_sidebar_state = 'collapsed')
 
  
st.image('bannerflai.jpg', use_column_width = 'always')


st.markdown('''
	# Ranking da 5ª Competição de Machine Learning FLAI 

	###### *Última Atualização: 11/09/2021
	
	---
''')

rank = pd.read_csv('4compMLflairank.csv')
subm = pd.read_csv('4compMLflai.csv')


#rank.index = rank['Nome']
#rank.drop(['Nome'], axis = 1, inplace = True)

col1, col2 = st.beta_columns(2) 

if col1.button('RANKING GERAL DA COMPETIÇÃO'):
	st.markdown('---') 
	st.write(rank.to_html(index=False), unsafe_allow_html=True)

if col2.button('LISTAGEM DE TODAS AS SUBMISSÕES'):
	st.markdown('---') 
	stg.AgGrid(subm.round(5), height = 800, fit_columns_on_grid_load = True)

st.markdown('---') 

st.sidebar.image('logoflai.png')
st.sidebar.markdown('---')
st.sidebar.markdown('#### Versão 0.1.0')
