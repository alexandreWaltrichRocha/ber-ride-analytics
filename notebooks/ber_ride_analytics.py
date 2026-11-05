# ==========================================
# BER Ride Analytics - Análise Exploratória
# Autor: Alexandre Waltrich Rocha
# ==========================================

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. CONFIGURAÇÕES E PATHS (Windows-Safe)
# ==========================================
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"] # Fonte segura para Windows

# Resolve o caminho absoluto dinamicamente, independente de onde o script é chamado
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "ncr_ride_bookings.csv"
VIS_DIR = BASE_DIR / "visualizacao"

# Cria a pasta de visualização se não existir
VIS_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# 2. CARREGAMENTO E PREPARAÇÃO DOS DADOS
# ==========================================
print("🔄 Carregando dataset...")
try:
    df = pd.read_csv(CSV_PATH)
    print(f"✅ Dataset carregado com sucesso! Total de registros brutos: {len(df)}")
except FileNotFoundError:
    print(f"❌ Erro: Arquivo não encontrado em {CSV_PATH}")
    exit()

# Tratamento robusto de datas
df["datetime"] = pd.to_datetime(
    df["Date"].astype(str) + " " + df["Time"].astype(str), 
    errors="coerce"
)
df = df.dropna(subset=["datetime"]) # Remove linhas com datas inválidas
print(f"✅ Registros válidos após limpeza de datas: {len(df)}")

df["day"] = df["datetime"].dt.day_name()
df["month"] = df["datetime"].dt.month_name()
df["hour"] = df["datetime"].dt.hour

# ==========================================
# 3. GERAÇÃO DOS GRÁFICOS (Lote sem travar)
# ==========================================
print("🎨 Gerando visualizações...")

def salvar_grafico(nome_arquivo):
    """Função auxiliar para padronizar salvamento e liberar memória no Windows."""
    caminho_completo = VIS_DIR / nome_arquivo
    plt.tight_layout()
    plt.savefig(caminho_completo, dpi=300, bbox_inches="tight")
    plt.close() # CRÍTICO: Fecha a figura para não abrir janelas pop-up no Windows
    print(f"  ✔️ Salvo: {nome_arquivo}")

# 3.1 Corridas por dia da semana
top_dias = df["day"].value_counts().nlargest(7).reset_index()
top_dias.columns = ["Dia", "Quantidade"]
sns.barplot(data=top_dias, x="Quantidade", y="Dia", palette="Set2")
plt.title("Top Dias da Semana com Mais Corridas")
plt.xlabel("Quantidade de Corridas")
plt.ylabel("Dia da Semana")
salvar_grafico("top_dias.png")

# 3.2 Corridas por mês
top_meses = df["month"].value_counts().nlargest(12).reset_index()
top_meses.columns = ["Mês", "Quantidade"]
sns.barplot(data=top_meses, x="Quantidade", y="Mês", palette="Set3")
plt.title("Corridas por Mês")
plt.xlabel("Quantidade de Corridas")
plt.ylabel("Mês")
salvar_grafico("top_meses.png")

# 3.3 Corridas por hora
top_horas = df["hour"].value_counts().sort_index().reset_index()
top_horas.columns = ["Hora", "Quantidade"]
sns.barplot(data=top_horas, x="Hora", y="Quantidade", palette="viridis")
plt.title("Distribuição de Corridas por Hora do Dia")
plt.xlabel("Hora (0-23)")
plt.ylabel("Quantidade")
salvar_grafico("top_horas.png")

# 3.4 Status das corridas (Barra)
if "Booking Status" in df.columns:
    top_status = df["Booking Status"].value_counts().nlargest(10).reset_index()
    top_status.columns = ["Status", "Quantidade"]
    sns.barplot(data=top_status, x="Quantidade", y="Status", palette="Set2")
    plt.title("Top 10 Status das Corridas")
    salvar_grafico("top10_status_bar.png")

    # 3.5 Status das corridas (Pizza)
    plt.figure(figsize=(8, 8))
    plt.pie(
        top_status["Quantidade"],
        labels=top_status["Status"],
        autopct="%1.1f%%",
        colors=sns.color_palette("Set2")
    )
    plt.title("Percentual dos Top 10 Status das Corridas")
    salvar_grafico("top10_status_pie.png")

# 3.6 Distribuição dos preços
if "Booking Value" in df.columns:
    df_preco = df[df["Booking Value"] >= 0]
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_preco, x="Booking Value", bins=50, kde=True, color="skyblue")
    plt.title("Distribuição dos Preços das Corridas")
    plt.xlabel("Valor da Corrida")
    salvar_grafico("distribuicao_precos.png")

    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df_preco, x="Booking Value", color="lightgreen")
    plt.title("Boxplot dos Preços das Corridas (Identificação de Outliers)")
    plt.xlabel("Valor da Corrida")
    salvar_grafico("boxplot_precos.png")

# 3.7 Top origens
if "Pickup Location" in df.columns:
    top_origens = df["Pickup Location"].value_counts().nlargest(10).reset_index()
    top_origens.columns = ["Origem", "Quantidade"]
    sns.barplot(data=top_origens, x="Quantidade", y="Origem", palette="Set2")
    plt.title("Top 10 Origens das Corridas")
    salvar_grafico("top10_origens.png")

# 3.8 Top destinos
if "Drop Location" in df.columns:
    top_destinos = df["Drop Location"].value_counts().nlargest(10).reset_index()
    top_destinos.columns = ["Destino", "Quantidade"]
    sns.barplot(data=top_destinos, x="Quantidade", y="Destino", palette="Set3")
    plt.title("Top 10 Destinos das Corridas")
    salvar_grafico("top10_destinos.png")

# 3.9 Série temporal (Top dias específicos)
corridas_por_dia = df.groupby(df["datetime"].dt.date).size().reset_index()
corridas_por_dia.columns = ["Data", "Quantidade"]
top_dias_corridas = corridas_por_dia.nlargest(10, "Quantidade")

plt.figure(figsize=(12, 6))
sns.barplot(data=top_dias_corridas, x="Data", y="Quantidade", color="steelblue")
plt.title("Top 10 Datas Específicas com Mais Corridas")
plt.xlabel("Data")
plt.ylabel("Quantidade de Corridas")
plt.xticks(rotation=45)
salvar_grafico("top10_dias_corridas.png")

# ==========================================
# 4. FINALIZAÇÃO
# ==========================================
print("\n" + "="*50)
print("✅ Análises concluídas com sucesso!")
print(f"📂 Gráficos salvos em: {VIS_DIR.resolve()}")
print("="*50)