import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dash do Fino", page_icon="♙", layout="wide")

@st.cache_data
def carregar_base():
    base = pd.read_csv("bases/inf_mensal_fidc_tab_I_202411.csv",encoding='latin1', sep=";")
    return base

base_df = carregar_base()

st.title("Dash de Exemplo para o Fino")

columns_with_tab = [col for col in base_df.columns if "TAB" in col]

coluna_dados = st.multiselect("Selecione a coluna de Dados", columns_with_tab)

grouby_data = base_df.groupby(["ADMIN","DT_COMPTC"])[coluna_dados].sum()

st.dataframe(grouby_data)


