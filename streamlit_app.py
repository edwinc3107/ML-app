import streamlit as st
import pandas as pd

st.title('🐧 Club Penguin - experiment with ML')

st.info('Play around with our factor drivers, to see cool visuals')

with st.expander("Our Data"):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write("X-axis")
  X= df.drop("species")
  X

  st.write("Y-axis")
  Y = df['species']
  Y
