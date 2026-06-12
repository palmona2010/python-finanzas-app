import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score, confusion_matrix, classification_report

st.set_page_config(page_title="Machine Learning", page_icon="🤖", layout="wide")

st.title("🤖 Machine Learning crediticio")

st.markdown("Ejemplo base de clasificación supervisada para scoring crediticio.")

n = st.slider("Número de observaciones", 500, 5000, 1000, 100)
modelo = st.selectbox("Modelo", ["Regresión logística", "Árbol de decisión"])

X, y = make_classification(
    n_samples=n,
    n_features=6,
    n_informative=4,
    n_redundant=1,
    weights=[0.75, 0.25],
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

if modelo == "Regresión logística":
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_scaled, y_train)
    probas = clf.predict_proba(X_test_scaled)[:, 1]
    preds = clf.predict(X_test_scaled)
else:
    clf = DecisionTreeClassifier(max_depth=4, random_state=42)
    clf.fit(X_train, y_train)
    probas = clf.predict_proba(X_test)[:, 1]
    preds = clf.predict(X_test)

auc = roc_auc_score(y_test, probas)
cm = confusion_matrix(y_test, preds)

st.metric("ROC-AUC", f"{auc:.3f}")

st.subheader("Matriz de confusión")
st.dataframe(pd.DataFrame(cm, index=["Real 0", "Real 1"], columns=["Pred 0", "Pred 1"]))

st.subheader("Reporte de clasificación")
st.text(classification_report(y_test, preds))