import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Monte Carlo", page_icon="🎲", layout="wide")

st.title("🎲 Simulación Monte Carlo de precios")

col1, col2, col3 = st.columns(3)

with col1:
    s0 = st.number_input("Precio inicial", value=100.0)
    mu = st.slider("Retorno esperado anual", -0.20, 0.50, 0.10, 0.01)

with col2:
    sigma = st.slider("Volatilidad anual", 0.01, 1.00, 0.25, 0.01)
    dias = st.slider("Horizonte en días", 30, 756, 252)

with col3:
    n_sim = st.slider("Número de simulaciones", 100, 5000, 1000, 100)
    seed = st.number_input("Semilla", value=42)

np.random.seed(int(seed))
dt = 1 / 252

shocks = np.random.normal(
    loc=(mu - 0.5 * sigma ** 2) * dt,
    scale=sigma * np.sqrt(dt),
    size=(dias, n_sim)
)

precios = s0 * np.exp(np.cumsum(shocks, axis=0))
df = pd.DataFrame(precios)

st.line_chart(df.iloc[:, :50])

final = df.iloc[-1]
st.metric("Precio esperado final", f"{final.mean():,.2f}")
st.metric("Percentil 5%", f"{final.quantile(0.05):,.2f}")
st.metric("Percentil 95%", f"{final.quantile(0.95):,.2f}")