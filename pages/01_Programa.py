import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Programa", page_icon="📚", layout="wide")

st.title("📚 Programa del curso")

html_path = Path("python_finanzas_programa_completo.html")

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")
    components.html(html_content, height=1500, scrolling=True)
else:
    st.error("No se encontró el archivo python_finanzas_programa_completo.html")