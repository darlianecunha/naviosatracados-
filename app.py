import streamlit as st
from datetime import datetime, timedelta

# Configurar o estilo do texto
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: #006400 !important;
}
</style>
""", unsafe_allow_html=True)

# Título do app com ícone de navio
st.markdown('<p class="big-font">🚢 Calculadora de Emissões Portuárias</p>', unsafe_allow_html=True)

# Explicação inicial
st.markdown('<p class="big-font">Preencha os campos abaixo para calcular os resultados de emissões portuárias automaticamente.</p>', unsafe_allow_html=True)

# Criar abas
abas = st.tabs(["Cálculo Padrão", "Simulação de Dias de Atracação"])

# Aba 1: Cálculo Padrão
with abas[0]:
    # Entradas do usuário
    st.header("Entradas")
    codigo_entrada = st.text_input("Código de Entrada")
    dtw = st.number_input("DTW (Deadweight Tonnage)", min_value=0.0, step=0.1)
    categoria = st.selectbox("Categoria", ["Granel Líquido", "Granel Sólido", "Carga Geral", "Container"])
    data_atracacao = st.text_input("Data de Atracação (dd/mm/yyyy HH:MM)")
    data_desatracacao = st.text_input("Data de Desatracação (dd/mm/yyyy HH:MM)")

    # Cálculo do P. Motor Auxiliar (kW)
    if categoria:
        if categoria == "Granel Líquido":
            p_motor_aux = 200
        elif categoria == "Granel Sólido":
            p_motor_aux = 150
        elif categoria == "Carga Geral":
            p_motor_aux = 100
        elif categoria == "Container":
            p_motor_aux = 250
    else:
        p_motor_aux = 0

    # Validação de datas e cálculos
    if codigo_entrada and dtw > 0 and categoria and data_atracacao and data_desatracacao:
        try:
            # Conversão de strings para datetime
            atracacao = datetime.strptime(data_atracacao, "%d/%m/%Y %H:%M")
            desatracacao = datetime.strptime(data_desatracacao, "%d/%m/%Y %H:%M")
            
            # Cálculo do tempo de atracação em horas
            tempo_atracacao = desatracacao - atracacao
            horas_atracacao = tempo_atracacao.total_seconds() / 3600
            
            # Cálculos ajustados
            energia_consumida = horas_atracacao * p_motor_aux
            mgo_consumido_t = dtw * horas_atracacao * 10 / 1_000_000
            co2_liberado_t = mgo_consumido_t * 3.2

            # Resultados
            st.header("Resultados")
            st.markdown(f'<p class="big-font"><strong>Código de Entrada:</strong> {codigo_entrada}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="big-font"><strong>DTW (Deadweight Tonnage):</strong> {dtw}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="big-font"><strong>Categoria:</strong> {categoria}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="big-font"><strong>P. Motor Auxiliar (kW):</strong> {p_motor_aux}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="big-font"><strong>Tempo de Atracação:</strong> {tempo_atracacao}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="big-font"><strong>Horas de Atracação:</strong> {horas_atracacao:.2f}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="big-font"><strong>Energia Consumida (kWh):</strong> {energia_consumida:.2f}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="big-font"><strong>MGO Consumido (t):</strong> {mgo_consumido_t:.2f}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="big-font"><strong>CO2 Liberado (t):</strong> {co2_liberado_t:.2f}</p>', unsafe_allow_html=True)

        except ValueError:
            st.error("Por favor, insira as datas no formato correto: dd/mm/yyyy HH:MM.")
    else:
        st.write("Preencha todas as informações para calcular os resultados.")

# Aba 2: Simulação de Dias de Atracação
with abas[1]:
    st.header("Simulação de Dias de Atracação")

    dias_simulados = st.number_input("Alterar dias de atracação:", min_value=
