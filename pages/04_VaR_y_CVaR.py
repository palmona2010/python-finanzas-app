import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="VaR y CVaR", page_icon="⚠️", layout="wide")

st.title("⚠️ Cálculo de VaR y CVaR")

st.markdown("Puedes subir un archivo CSV con una columna de retornos o usar datos simulados.")

uploaded = st.file_uploader("Subir CSV", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded)
    columna = st.selectbox("Selecciona la columna de retornos", df.columns)
    returns = df[columna].dropna()
else:
    np.random.seed(42)
    returns = pd.Series(np.random.normal(0.0005, 0.02, 1000), name="retornos_simulados")

confianza = st.slider("Nivel de confianza", 0.90, 0.99, 0.95, 0.01)

var = -np.quantile(returns, 1 - confianza)
cvar = -returns[returns <= np.quantile(returns, 1 - confianza)].mean()

col1, col2 = st.columns(2)
col1.metric("VaR histórico", f"{var:.2%}")
col2.metric("CVaR histórico", f"{cvar:.2%}")

st.line_chart(returns)
st.bar_chart(returns)