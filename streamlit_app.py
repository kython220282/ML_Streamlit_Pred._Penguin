import streamlit as st
import pandas as pd

#st.set_page_config(layout="wide")

st.title('ML App.: Predict Penguin Species')
st.info('This application predicts Penguin species based on the input features selected by the user in the sidebar!')
st.write('By: Karan Raj Sharma')
st.write('--------')
st.warning('Please enter your inputs in the sidebar. Expand sidebar to view input fields')

with st.expander('Data'):
  st.write('**Raw Data**')

  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
 
  st.write('**X**')
  X= df.drop('species',axis = 1)
  X

  st.write('**y**')
  y= df.species
  y
  y

with st.expander('Data Visualisation'):
  st.scatter_chart(data = df, x = 'bill_depth_mm', y = 'bill_length_mm', color='species')
  st.scatter_chart(data = df, x = 'bill_depth_mm', y = 'bill_length_mm', color='island')

# Data Prepration
with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Home Island',('Biscoe','Dream','Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)',13.1,21.50,17.2)
  flipper_length_mm = st.slider('Flipper length (mm)',172,231,201)
  body_mass_g = st.slider('Body mass (g)', 2700, 6300, 4207)
  sex = st.selectbox('gender',('male','female'))
  
  # Create a DataFrame for the input features
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': sex}
  input_df = pd.DataFrame(data,index=[0])
  input_penguins = pd.concat([input_df,X],axis=0)
  
 #Encode Categorical Variables
st.write('**Encoded Categorical Features**')
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
input_row = df_penguins[:1]

#Encode y 
target_mapper = {'Adelie':0,
                 'Chinstrap':1,
                 'Gentoo':2}
def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)
y


with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguins data**')
  input_penguins
  st.write('**Encoded input penguin**')
  input_row

