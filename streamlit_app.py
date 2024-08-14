import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#st.set_page_config(layout="wide")

st.title('ML App.: Predict Penguin Species')
st.info('This application predicts Penguin species based on the input features selected by the user in the sidebar!')
st.write('By: Karan Raj Sharma')
st.write('--------')
st.warning('Please enter your inputs in the sidebar. Expand sidebar on the left to view input fields. The predicted species will reflect in the "Predicted Species" section below')

with st.expander('Data'):
  st.write('**Raw Data**')

  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
 
  st.write('**X**')
  X_raw= df.drop('species',axis = 1)
  X_raw

  st.write('**y**')
  y_raw= df.species
  y_raw

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
  input_penguins = pd.concat([input_df,X_raw],axis=0)

with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguins data**')
  input_penguins
  
#Data Prepration  

#Encode Categorical Variables (X)
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)

X= df_penguins[1:]
input_row = df_penguins[:1]

#Encode y 
target_mapper = {'Adelie':0,
                 'Chinstrap':1,
                 'Gentoo':2}
def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)

with st.expander('Data prepration'):
  st.write('**Encoded input penguin (X)**')
  input_row
  st.write('**Encoded y**')
  y

# Machine Learning Model Training and inference
#Train the model
clf = RandomForestClassifier()
clf.fit(X,y)

#Apply model to make prediction
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie','Chinstrap','Gentoo']
df_prediction_proba.rename(columns={0:'Adelie',
                                 1:'Chinstrap',
                                 2:'Gentoo'})

# Display Predicted species
st.subheader('Predicted Species')
st.write('**Probablity Score**')
st.dataframe(df_prediction_proba,
             column_config={
               'Adelie': st.column_config.ProgressColumn(
                 'Adelie',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
               'Chinstrap': st.column_config.ProgressColumn(
                 'Chinstrap',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
               'Gentoo': st.column_config.ProgressColumn(
                 'Gentoo',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),  
             },hide_index=True)

penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write('**Prediction**')
st.success(str(penguins_species[prediction][0]))




