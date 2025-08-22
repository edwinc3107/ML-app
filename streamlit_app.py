import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

st.title('🐧 Club Penguin - experiment with ML')

st.info('Play around with our factor drivers, to see cool visuals')

with st.expander("Our Data"):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write("X-axis")
  X_raw= df.drop("species", axis = 1)
  X_raw

  st.write("Y-axis")
  Y_raw = df.species
  Y_raw
with st.expander("Visualize"):
  option = st.selectbox(
    "X-axis",
    ("species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"),
)
  option2 = st.selectbox(
    "Y-axis",
    ("species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"),
)
  option3 = st.selectbox(
    "Type",
    ('area_chart','bar_chart','line_chart','scatter_chart'),
)
  st.write("Graph")
  
  st.scatter_chart(data= df, x=option, y= option2, color='species')


with st.sidebar:
  st.header("Features")
  gender = st.selectbox("Gender", ("Male", "Female"))
  island = st.selectbox("Island", ("Biscoe","Dream","Torgersen"))
  bill_length_mm = st.slider("Bill length (mm)",32.1,59.6,43.9)
  bill_depth_mm = st.slider("Bill depth (mm)",13.1, 21.5,17.2)
  flipper_length_mm = st.slider("Flipper length (mm)",172.0, 231.0,201.0)
  body_mass_g = st.slider("Body mass (g)",2700.0, 6300.0, 4207.0)



data = {
  'island': island,
  'bill_length_mm': bill_length_mm,
  'bill_depth_mm' : bill_depth_mm,
  'flipper_length_mm' : flipper_length_mm,
  'body_mass_g' : body_mass_g,
  'sex' : gender
}

input_dataframe = pd.DataFrame(data, index=[0])

input_joined = pd.concat([input_dataframe, X_raw], axis = 0)

with st.expander("Input Features"):
  st.write('Input Dataframe')
  input_dataframe
  st.write('New Dataframe')
  input_joined

#Data Prep

#Encode

encode = ['island','sex'] # strings need to be encoded
df_penguins = pd.get_dummies(input_joined, prefix = encode)

input_X = df_penguins[1:]
input_row = df_penguins[:1]

#Encode Y

map= {
  "Adelie":0,
  "Chinstrap":1,
  "Gentoo": 2,
}

def target(val):
  return map[val]

Y = Y_raw.apply(target)

with st.expander("Data Preparation"):
  st.write("Encoded X")
  input_row
  st.write("Encoded Y")
  Y

#Model Training
#Because classification type problem - we use RandomForestClassifier

model = RandomForestClassifier()

#fit into model
model.fit(input_X,Y)

#predict

prediction = model.predict(input_row)
probability = model.predict_proba(input_row)

probability








  
  
  

  
