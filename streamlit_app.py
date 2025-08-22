import streamlit as st
import pandas as pd

st.title('🐧 Club Penguin - experiment with ML')

st.info('Play around with our factor drivers, to see cool visuals')

with st.expander("Our Data"):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write("X-axis")
  X= df.drop("species", axis = 1)
  X

  st.write("Y-axis")
  Y = df.species
  Y
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
  
  
  
  

  
