import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 



st.set_page_config(
    page_title="Cargatron",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",

    
)

st.title("De los creadores de Tuprima, llega.... ¡CARGATRON!")

df = pd.read_csv("./data/red_recarga_acceso_publico_2021.csv",sep=";")
st.write(df)

with st.expander("See explanation"):
    st.image("kratos.jpg", caption="Kratos")

