import streamlit as st
import pandas as pd

# Título do app
st.title("Calculadora de Emissões Portuárias")

# Seção de upload de arquivo
st.sidebar.header("Upload de Arquivo")
uploaded_file = st.sidebar.file_uploader("Faça upload da planilha (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    # Carregar planilha
    data = pd.ExcelFile(uploaded_file)
    sheet_options = data.sheet_names
    selected_sheet = st.sidebar.selectbox("Selecione a aba", sheet_options)
    df = data.parse(selected_sheet)
    st.write("Dados carregados da planilha:")
    st.dataframe(df)
else:
    # Caso não haja upload, iniciar com um DataFrame vazio
    df = pd.DataFrame(columns=[
        "Nº ENTRADA", "NAVIO", "CARGA", "TEMPO ATRACADO (h)", 
        "CONSUMO HFO (g)", "CONSUMO MGO/MDO (g)", "EMISSÕES (t)"
    ])
    st.write("Nenhuma planilha carregada. Insira dados manualmente.")

# Entrada manual de dados
st.header("Inserir Dados Manualmente")
with st.form("manual_entry"):
    num_entrada = st.text_input("Número de Entrada")
    navio = st.text_input("Nome do Navio")
    carga = st.selectbox("Tipo de Carga", ["GRANEL LÍQUIDO", "GRANEL SÓLIDO", "CARGA GERAL"])
    tempo_atracado = st.number_input("Tempo Atracado (em horas)", min_value=0.0)
    consumo_hfo = st.number_input("Consumo de HFO (em gramas)", min_value=0.0)
    consumo_mgo = st.number_input("Consumo de MGO/MDO (em gramas)", min_value=0.0)
    
    submitted = st.form_submit_button("Adicionar Entrada")
    if submitted:
        # Adicionar os dados ao DataFrame
        new_entry = {
            "Nº ENTRADA": num_entrada,
            "NAVIO": navio,
            "CARGA": carga,
            "TEMPO ATRACADO (h)": tempo_atracado,
            "CONSUMO HFO (g)": consumo_hfo,
            "CONSUMO MGO/MDO (g)": consumo_mgo,
            "EMISSÕES (t)": (consumo_hfo + consumo_mgo) / 1_000_000  # Exemplo de cálculo
        }
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        st.success("Entrada adicionada com sucesso!")

# Exibir os dados
st.header("Dados Atuais")
st.dataframe(df)

# Cálculo de emissões
if not df.empty:
    st.header("Cálculo de Emissões")
    if st.button("Calcular"):
        df["EMISSÕES (t)"] = (df["CONSUMO HFO (g)"] + df["CONSUMO MGO/MDO (g)"]) / 1_000_000
        st.write("Resultados Atualizados:")
        st.dataframe(df)

# Opção para exportar os resultados
if not df.empty:
    st.header("Exportar Resultados")
    if st.button("Exportar para Excel"):
        df.to_excel("resultados_calculados.xlsx", index=False)
        st.success("Arquivo exportado!")
