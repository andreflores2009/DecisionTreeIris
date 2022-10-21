import streamlit as st

st.title("Aplicativo de IA")
nome = st.text_input("Digite o nome")
if st.button("Clique aqui"):
  st.write("Bem vindo", nome, "ao seu primeiro aplicativo")
