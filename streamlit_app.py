import streamlit as st
import pandas as pd

#st.set_page_config(layout="wide")

st.title('Machine Learning Application')
st.info('This application builds a Machine learning model !')
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

with st.expander('Data Visualisation'):
  st.scatter_chart(data = df, x = 'bill_depth_mm', y = 'bill_length_mm', color='species')
  st.scatter_chart(data = df, x = 'bill_depth_mm', y = 'bill_length_mm', color='island')

# Data Prepration
with st.sidebar:
  #island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  sex = st.selectbox('gender',('male','female'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)',13.1,21.50,17.2)
  flipper_length_mm = st.slider('Flipper length (mm)',172,231,201)
  body_mass_g = st.slider('Body mass (g)', 2700, 6300, 4207)
                        

