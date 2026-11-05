import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# 1. CONFIGURAÇÃO DA PÁGINA
# =====================================
st.set_page_config(
    page_title="BER Ride Analytics",
    page_icon="🚕",
    layout="wide"
)

# =====================================
# 2. LEITURA E TRATAMENTO DOS DADOS
# =====================================
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv("data/ncr_ride_bookings.csv")
        
        # Tratamento robusto de datas (evita falhas com valores nulos ou formatos estranhos)
        df["datetime"] = pd.to_datetime(
            df["Date"].astype(str) + " " + df["Time"].astype(str), 
            errors="coerce"
        )
        
        # Remove linhas onde a data/hora falhou ao converter
        df = df.dropna(subset=["datetime"])
        
        df["hour"] = df["datetime"].dt.hour
        df["day"] = df["datetime"].dt.day_name()
        
        # Mapeamento para Português
        dias_pt = {
            "Monday": "Segunda-feira", "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira", "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira", "Saturday": "Sábado", "Sunday": "Domingo"
        }
        df["day"] = df["day"].map(dias_pt).fillna("Desconhecido")
        
        return df
    except FileNotFoundError:
        st.error("Arquivo 'data/ncr_ride_bookings.csv' não encontrado. Verifique o caminho.")
        return pd.DataFrame()

df_base = carregar_dados()

# Se o dataframe estiver vazio (erro no carregamento), para a execução
if df_base.empty:
    st.stop()

# =====================================
# 3. SIDEBAR E FILTROS
# =====================================
st.sidebar.title("🎛️ Filtros")

# Criamos uma cópia para aplicar os filtros e evitar o warning SettingWithCopy do Pandas
df = df_base.copy()

# FILTRO: STATUS
if "Booking Status" in df.columns:
    status_opcoes = ["Todos"] + sorted(df["Booking Status"].dropna().unique().tolist())
    status_escolhido = st.sidebar.selectbox("Status da Corrida", status_opcoes)
    if status_escolhido != "Todos":
        df = df[df["Booking Status"] == status_escolhido].copy()

# FILTRO: VEÍCULO
if "Vehicle Type" in df.columns:
    veiculo_opcoes = ["Todos"] + sorted(df["Vehicle Type"].dropna().unique().tolist())
    veiculo_escolhido = st.sidebar.selectbox("Tipo de Veículo", veiculo_opcoes)
    if veiculo_escolhido != "Todos":
        df = df[df["Vehicle Type"] == veiculo_escolhido].copy()

# =====================================
# 4. TÍTULO E KPIS
# =====================================
st.title("🚕 BER Ride Analytics")
st.markdown("Dashboard interativo para análise de mobilidade urbana.")
st.divider()

st.subheader("📊 Indicadores (KPIs)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Corridas", f"{len(df):,}")
with col2:
    st.metric("Dias Distintos", f"{df['Date'].nunique():,}")
with col3:
    if "Booking Value" in df.columns:
        receita = df["Booking Value"].sum()
        st.metric("Receita Total", f"R$ {receita:,.2f}")
    else:
        st.metric("Receita Total", "N/A")
with col4:
    if "Booking Value" in df.columns:
        ticket_medio = df["Booking Value"].mean()
        st.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")
    else:
        st.metric("Ticket Médio", "N/A")

st.divider()

# =====================================
# 5. GRÁFICOS
# =====================================
col1, col2 = st.columns(2)

# 5.1 Corridas por Hora
with col1:
    corridas_hora = df["hour"].value_counts().sort_index().reset_index()
    corridas_hora.columns = ["Hora", "Quantidade"]
    fig_hora = px.bar(corridas_hora, x="Hora", y="Quantidade", title="Corridas por Hora do Dia")
    st.plotly_chart(fig_hora, use_container_width=True)

# 5.2 Corridas por Dia da Semana
with col2:
    ordem_dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    corridas_dia = df["day"].value_counts().reindex(ordem_dias).dropna().reset_index()
    corridas_dia.columns = ["Dia", "Quantidade"]
    
    fig_dia = px.bar(corridas_dia, x="Quantidade", y="Dia", orientation="h", title="Corridas por Dia da Semana")
    st.plotly_chart(fig_dia, use_container_width=True)

# 5.3 Distribuição dos Status
if "Booking Status" in df.columns:
    st.subheader("📈 Análise Operacional")
    col3, col4 = st.columns(2)
    
    with col3:
        status_counts = df["Booking Status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Quantidade"]
        fig_status = px.pie(status_counts, values="Quantidade", names="Status", title="Distribuição dos Status")
        st.plotly_chart(fig_status, use_container_width=True)

# 5.4 Top 10 Destinos
if "Drop Location" in df.columns:
    with col4:
        destinos = df["Drop Location"].value_counts().head(10).reset_index()
        destinos.columns = ["Destino", "Quantidade"]
        fig_destino = px.bar(destinos, x="Quantidade", y="Destino", orientation="h", title="Top 10 Destinos")
        st.plotly_chart(fig_destino, use_container_width=True)

# 5.5 Top 10 Origens
if "Pickup Location" in df.columns:
    st.subheader("📍 Análise Geográfica")
    col5, col6 = st.columns(2)
    
    with col5:
        origens = df["Pickup Location"].value_counts().head(10).reset_index()
        origens.columns = ["Origem", "Quantidade"]
        fig_origem = px.bar(origens, x="Quantidade", y="Origem", orientation="h", title="Top 10 Origens")
        st.plotly_chart(fig_origem, use_container_width=True)

# 5.6 Distribuição dos Preços
if "Booking Value" in df.columns:
    with col6:
        df_limpo = df[df["Booking Value"] >= 0]
        fig_preco = px.histogram(df_limpo, x="Booking Value", nbins=50, title="Distribuição dos Preços das Corridas")
        st.plotly_chart(fig_preco, use_container_width=True)

# =====================================
# 6. TABELA DE DADOS
# =====================================
st.divider()
st.subheader("📋 Amostra dos Dados Filtrados")
st.dataframe(
    df.head(50),
    use_container_width=True,
    hide_index=True
)