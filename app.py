import streamlit as st
import pandas as pd

# Título do app
st.title("Calculadora de Emissões Portuárias")

# Modelo de entrada e cálculo baseado na aba "2022"
st.sidebar.header("Modelo de Entradas")
st.sidebar.write("Entradas obrigatórias para cálculo:")

# Definindo entradas conforme a planilha
inputs = {
    "input1": st.sidebar.text_input("Nº Entrada"),
    "input2": st.sidebar.text_input("Navio"),
    "input3": st.sidebar.selectbox("Tipo de Carga", ["GRANEL LÍQUIDO", "GRANEL SÓLIDO", "CARGA GERAL"]),
    "input4": st.sidebar.number_input("Tempo Atracado (em horas)", min_value=0.0, step=0.1),
    "input5": st.sidebar.number_input("Consumo de HFO (em gramas)", min_value=0.0, step=0.1),
    "input6": st.sidebar.number_input("Consumo de MGO/MDO (em gramas)", min_value=0.0, step=0.1),
}

# Botão para adicionar entradas
st.sidebar.header("Adicionar Entrada")
add_entry = st.sidebar.button("Adicionar aos Dados")

# Dados para armazenar entradas
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["Nº Entrada", "Navio", "Tipo de Carga", 
                                                     "Tempo Atracado (h)", "Consumo HFO (g)", 
                                                     "Consumo MGO/MDO (g)", "Cal1", "Cal2", "Cal3"])

# Adicionando entradas aos dados
if add_entry:
    new_data = {
        "Nº Entrada": inputs["input1"],
        "Navio": inputs["input2"],
        "Tipo de Carga": inputs["input3"],
        "Tempo Atracado (h)": inputs["input4"],
        "Consumo HFO (g)": inputs["input5"],
        "Consumo MGO/MDO (g)": inputs["input6"],
        "Cal1": inputs["input4"] * 0.5,  # Exemplo fictício para Cal1
        "Cal2": inputs["input5"] / 1_000_000,  # Exemplo fictício para Cal2
        "Cal3": inputs["input6"] / 1_000_000,  # Exemplo fictício para Cal3
    }
    st.session_state["data"] = pd.concat([st.session_state["data"], pd.DataFrame([new_data])], ignore_index=True)
    st.success("Entrada adicionada com sucesso!")

# Mostrar os dados atuais
st.header("Dados Inseridos")
st.dataframe(st.session_state["data"])

# Cálculos de emissões
if not st.session_state["data"].empty:
    st.header("Cálculos de Emissões")
    st.write("Resultados Calculados com base no modelo:")
    st.dataframe(st.session_state["data"])

# Exportar dados calculados
st.header("Exportar Resultados")
if st.button("Exportar para Excel"):
    st.session_state["data"].to_excel("resultados_calculados.xlsx", index=False)
    st.success("Arquivo exportado com sucesso!")



