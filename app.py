import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# CONFIGURAÇÃO
# =====================================

st.set_page_config(
    page_title="BER Ride Analytics",
    page_icon="🚕",
    layout="wide"
)

# =====================================
# LEITURA DOS DADOS
# =====================================

@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/ncr_ride_bookings.csv")

    df["datetime"] = pd.to_datetime(
        df["Date"] + " " + df["Time"]
    )

    df["hour"] = df["datetime"].dt.hour
    df["day"] = df["datetime"].dt.day_name()

    dias_pt = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }

    df["day"] = df["day"].map(dias_pt)

    return df


df = carregar_dados()

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🎛️ Filtros")

# STATUS

if "Booking Status" in df.columns:

    status_opcoes = ["Todos"] + sorted(
        df["Booking Status"]
        .dropna()
        .unique()
        .tolist()
    )

    status_escolhido = st.sidebar.selectbox(
        "Status da Corrida",
        status_opcoes
    )

    if status_escolhido != "Todos":
        df = df[
            df["Booking Status"]
            == status_escolhido
        ]

# VEÍCULO

if "Vehicle Type" in df.columns:

    veiculo_opcoes = ["Todos"] + sorted(
        df["Vehicle Type"]
        .dropna()
        .unique()
        .tolist()
    )

    veiculo_escolhido = st.sidebar.selectbox(
        "Tipo de Veículo",
        veiculo_opcoes
    )

    if veiculo_escolhido != "Todos":
        df = df[
            df["Vehicle Type"]
            == veiculo_escolhido
        ]

# =====================================
# TÍTULO
# =====================================

st.title("🚕 BER Ride Analytics")

st.markdown(
    "Dashboard interativo para análise de mobilidade urbana."
)

# =====================================
# KPIs
# =====================================

st.subheader("📊 Indicadores")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total de Corridas",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Total de Colunas",
        len(df.columns)
    )

with col3:
    st.metric(
        "Dias Distintos",
        df["Date"].nunique()
    )

st.divider()

# =====================================
# GRÁFICOS
# =====================================

col1, col2 = st.columns(2)

# CORRIDAS POR HORA

with col1:

    corridas_hora = (
        df["hour"]
        .value_counts()
        .sort_index()
    )

    fig_hora = px.bar(
        x=corridas_hora.index,
        y=corridas_hora.values,
        title="Corridas por Hora",
        labels={
            "x": "Hora",
            "y": "Quantidade"
        }
    )

    st.plotly_chart(
        fig_hora,
        use_container_width=True
    )

# CORRIDAS POR DIA

with col2:

    corridas_dia = (
        df["day"]
        .value_counts()
    )

    fig_dia = px.bar(
        x=corridas_dia.values,
        y=corridas_dia.index,
        orientation="h",
        title="Corridas por Dia"
    )

    st.plotly_chart(
        fig_dia,
        use_container_width=True
    )

# =====================================
# STATUS
# =====================================

if "Booking Status" in df.columns:

    status = (
        df["Booking Status"]
        .value_counts()
    )

    fig_status = px.pie(
        values=status.values,
        names=status.index,
        title="Distribuição dos Status"
    )

    st.plotly_chart(
        fig_status,
        use_container_width=True
    )

# =====================================
# DESTINOS
# =====================================

if "Drop Location" in df.columns:

    destinos = (
        df["Drop Location"]
        .value_counts()
        .head(10)
    )

    fig_destino = px.bar(
        x=destinos.values,
        y=destinos.index,
        orientation="h",
        title="Top 10 Destinos"
    )

    st.plotly_chart(
        fig_destino,
        use_container_width=True
    )

# =====================================
# ORIGENS
# =====================================

if "Pickup Location" in df.columns:

    origens = (
        df["Pickup Location"]
        .value_counts()
        .head(10)
    )

    fig_origem = px.bar(
        x=origens.values,
        y=origens.index,
        orientation="h",
        title="Top 10 Origens"
    )

    st.plotly_chart(
        fig_origem,
        use_container_width=True
    )

# =====================================
# PREÇOS
# =====================================

if "Booking Value" in df.columns:

    fig_preco = px.histogram(
        df,
        x="Booking Value",
        nbins=30,
        title="Distribuição dos Preços"
    )

    st.plotly_chart(
        fig_preco,
        use_container_width=True
    )

# =====================================
# INSIGHTS
# =====================================

st.subheader("📈 Principais Insights")

st.info(f"""
Total analisado: {len(df):,} corridas.

Use os filtros à esquerda para explorar diferentes
status e tipos de veículos.
""")

# =====================================
# TABELA
# =====================================

st.subheader("📋 Amostra dos Dados")

st.dataframe(
    df.head(50),
    use_container_width=True
)
