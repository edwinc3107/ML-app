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
  type = st.selectbox(
    "Type",
    (area_chart,bar_chart,line_chart,scatter_chart),
)
  st.write("Graph")
  
  st.type(data= df, x=option, y= option2, color='species')


  
