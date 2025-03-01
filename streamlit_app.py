import streamlit as st
import pandas as pd

st.title('🤖 Machine learning app')

st.info('This app builds a ml model!')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df
