import streamlit as st
import os

aulas_dir = os.path.dirname(os.path.dirname(__file__))
aulas_dir = os.path.join(aulas_dir, "aulas")

cursos = []

for curso in os.listdir(aulas_dir):
    cursos.append(curso)

print(cursos)

st.title("Treinamentos Gratuitos")

st.markdown("---")

# Dropdown menu
selected_training = st.selectbox("Selecione um treinamento", cursos)

if selected_training:
    apostila_path = os.path.join(aulas_dir, selected_training, "apostila.md")
    if os.path.exists(apostila_path):
        with open(apostila_path, "r", encoding="utf-8") as f:
            content = f.read()
            st.markdown(content)
    else:
        st.warning("Arquivo apostila.md não encontrado neste curso.")
