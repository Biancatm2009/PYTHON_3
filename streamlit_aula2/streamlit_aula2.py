import streamlit as st
import pandas as pd

nome = st.text_input("Digite seu nome:") 
if nome:
 st.write("Olá,", nome) 

linha = st.selectbox(
"Escolha uma linha:",
["510", "520", "550"]
)

st.write("Linha selecionada:", linha) 
linhas = st.multiselect(
"Escolha as linhas:",
["510", "520", "550", "620"]
) 

st.write(linhas) 
if st.button("Calcular"):
 st.write("Calculando...")