import streamlit as st
import numpy as np
import pandas as pd
from scipy.optimize import minimize

st.set_page_config(page_title="Portafolios", page_icon="📊", layout="wide")

st.title("📊 Optimización de portafolios")

n_activos = st.slider("Número de activos", 2, 8, 4)
np.random.seed(42)

retornos_esperados = np.random.uniform(0.06, 0.20, n_activos)
cov = np.random.rand(n_activos, n_activos)
cov = np.dot(cov, cov.T) / 10

nombres = [f"Activo {i+1}" for i in range(n_activos)]

def port_return(w):
    return np.dot(w, retornos_esperados)

def port_vol(w):
    return np.sqrt(np.dot(w.T, np.dot(cov, w)))

def neg_sharpe(w):
    rf = 0.03
    return -(port_return(w) - rf) / port_vol(w)

constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}
bounds = [(0, 1)] * n_activos
w0 = np.repeat(1 / n_activos, n_activos)

result = minimize(neg_sharpe, w0, bounds=bounds, constraints=constraints)
weights = result.x

df = pd.DataFrame({
    "Activo": nombres,
    "Retorno esperado": retornos_esperados,
    "Peso óptimo": weights
})

st.dataframe(df, use_container_width=True)

st.metric("Retorno esperado del portafolio", f"{port_return(weights):.2%}")
st.metric("Volatilidad esperada", f"{port_vol(weights):.2%}")
st.metric("Sharpe aproximado", f"{-result.fun:.2f}")

st.bar_chart(df.set_index("Activo")["Peso óptimo"])