import streamlit as st
import pandas as pd

st.title('🤖 Machine learning app')

st.info('This app builds a ml model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

st.write('**X**')
X = df.drop('species', axis=1)
X

st.write('**y**')
y = df.species
y

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_m', y='body_mass_g', color='species')
  
