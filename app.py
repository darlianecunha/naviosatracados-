import streamlit as st
import pandas as pd

# Título do app
st.title("Calculadora de Emissões Portuárias")

# Mensagem inicial
st.write("Digite as informações abaixo e o programa calculará as emissões automaticamente.")

# Entradas do usuário
st.header("Entradas")
input1 = st.text_input("Nº Entrada")
input2 = st.text_input("Navio")
input3 = st.selectbox("Tipo de Carga", ["GRANEL LÍQUIDO", "GRANEL SÓLIDO", "CARGA GERAL"])
input4 = st.number_input("Tempo Atracado (em horas)", min_value=0.0, step=0.1)
input5 = st.number_input("Consumo de HFO (em gramas)", min_value=0.0, step=0.1)
input6 = st.number_input("Consumo de MGO/MDO (em gramas)", min_value=0.0, step=0.1)

# Realiza os cálculos automaticamente
if input1 and input2 and input3:
    st.header("Resultados")
    cal1 = input4 * 0.5  # Exemplo fictício para cálculo 1 (substitua conforme necessário)
    cal2 = input5 / 1_000_000  # Exemplo fictício para cálculo 2
    cal3 = input6 / 1_000_000  # Exemplo fictício para cálculo 3
    
    # Exibir os resultados
    results = {
        "Nº Entrada": input1,
        "Navio": input2,
        "Tipo de Carga": input3,
        "Tempo Atracado (h)": input4,
        "Consumo HFO (g)": input5,
        "Consumo MGO/MDO (g)": input6,
        "Cal1 (Resultado 1)": cal1,
        "Cal2 (Resultado 2)": cal2,
        "Cal3 (Resultado 3)": cal3,
    }
    st.write(pd.DataFrame([results]))
else:
    st.write("Por favor, preencha todas as informações para calcular os resultados.")
