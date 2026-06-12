import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Python para Finanzas",
    page_icon="📈",
    layout="wide"
)

st.sidebar.title("Python para Finanzas")
st.sidebar.markdown("EAFIT · Asobancaria")

st.title("App del curso: Python para Finanzas")

with open("python_finanzas_programa_completo.html", "r", encoding="utf-8") as file:
    html_content = file.read()

components.html(
    html_content,
    height=1400,
    scrolling=True
)
