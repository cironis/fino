import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dash do Fino", page_icon="♙", layout="wide")

@st.cache_data
def carregar_base():
    base = pd.read_csv("bases/extrato_fi.csv")
    return base

base_df = carregar_base()

st.title("Dash de Exemplo para o Fino")

st.dataframe(base_df)

