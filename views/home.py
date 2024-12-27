import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dash do Fino", page_icon="♙", layout="wide")

@st.cache_data
def carregar_base():
    base = pd.read_csv("bases/inf_mensal_fidc_tab_I_202411.csv",encoding='latin1', sep=";")
    return base

base_df = carregar_base()

st.title("Dash de Exemplo para o Fino")

st.subheader("Exemplo de filtros e Tabelas")

admins = base_df["ADMIN"].unique()

admins_select = st.selectbox("Selecione o Admin", admins)

base_df = base_df.loc[base_df["ADMIN"] == admins_select]

columns_with_tab = [col for col in base_df.columns if "TAB" in col]

coluna_dados_select = st.multiselect("Selecione a coluna de Dados", columns_with_tab)

grouby_data = base_df.groupby(["DT_COMPTC","DENOM_SOCIAL"])[coluna_dados_select].sum().reset_index()

st.dataframe(grouby_data,hide_index=True,use_container_width=True)

st.subheader("Exemplo de Gráfico")

coluna_grafico_select = st.selectbox("Selecione a Coluna para o Gráfico", columns_with_tab)

grouby_graph = base_df.groupby(["DENOM_SOCIAL"])[coluna_grafico_select].sum().reset_index()

fig = px.bar(
    grouby_graph,
    x="DENOM_SOCIAL",  # X-axis
    y=coluna_grafico_select,  # Y-axis is user-selected
    title=f"Gráfico da Coluna {coluna_grafico_select}",
    labels={"DENOM_SOCIAL": "Denominação Social", coluna_grafico_select: "Valor"},
    text_auto=True  # Automatically add text labels to bars
)

# Display the chart in Streamlit
st.plotly_chart(fig)
