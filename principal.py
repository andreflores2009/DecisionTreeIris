import streamlit as st

st.titulo("Aplicativo de IA")
nome = st.input_text("Digite o nome")

st.write("Bem vindo", nome, "ao seu primeiro aplicativo")
