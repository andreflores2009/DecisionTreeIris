import streamlit as st

st.titulo("Aplicativo de IA")
nome = st.text_input("Digite o nome")

st.write("Bem vindo", nome, "ao seu primeiro aplicativo")
