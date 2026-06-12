import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Bonos", page_icon="💵", layout="wide")

st.title("💵 Calculadora de bonos")

col1, col2, col3 = st.columns(3)

with col1:
    valor_nominal = st.number_input("Valor nominal", value=1000.0, min_value=0.0)
    tasa_cupon = st.slider("Tasa cupón anual", 0.0, 0.30, 0.08, 0.005)

with col2:
    ytm = st.slider("Yield to Maturity anual", 0.0, 0.30, 0.10, 0.005)
    madurez = st.slider("Madurez en años", 1, 30, 5)

with col3:
    frecuencia = st.selectbox("Frecuencia de pago", [1, 2, 4, 12], index=1)

n = madurez * frecuencia
cupon = valor_nominal * tasa_cupon / frecuencia
tasa_periodica = ytm / frecuencia

flujos = np.repeat(cupon, n)
flujos[-1] += valor_nominal
periodos = np.arange(1, n + 1)

precio = np.sum(flujos / (1 + tasa_periodica) ** periodos)
duracion_macaulay = np.sum(periodos * flujos / (1 + tasa_periodica) ** periodos) / precio / frecuencia

st.metric("Precio del bono", f"{precio:,.2f}")
st.metric("Duración de Macaulay", f"{duracion_macaulay:,.2f} años")

df = pd.DataFrame({
    "Periodo": periodos,
    "Flujo": flujos,
    "Valor presente": flujos / (1 + tasa_periodica) ** periodos
})

st.dataframe(df, use_container_width=True)
st.line_chart(df.set_index("Periodo")[["Flujo", "Valor presente"]])