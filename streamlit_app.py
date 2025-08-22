import streamlit as st
import pandas as pd

st.title('🐧 Club Penguin - experiment with ML')

st.info('Play around with our factor drivers, to see cool visuals')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
