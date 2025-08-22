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
  st.write("Graph")
  st.line_chart(df)
  
