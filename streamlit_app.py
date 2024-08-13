import streamlit as st
import pandas as pd

# st.set_page_config(layout="wide")

st.title('Machine Learning Application')
st.info('This application builds a Machine learning model!')
st.write('By: Karan Raj Sharma')
st.write('--------')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

st.write('**X**')
X= df.drop('species',axis = 1)
X

st.write('**y**')
y= df.species
y
