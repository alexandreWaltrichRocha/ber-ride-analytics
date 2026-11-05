# ==========================================
# BER Ride Analytics
# Autor: Alexandre Waltrich Rocha
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Configurações
# ==========================================

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSV_PATH = os.path.join(
    BASE_DIR,
    "data",
    "ncr_ride_bookings.csv"
)

VIS_DIR = os.path.join(
    BASE_DIR,
    "visualizacao"
)

os.makedirs(VIS_DIR, exist_ok=True)

# ==========================================
# Carregamento do dataset
# ==========================================

print("Carregando dataset...")

df = pd.read_csv(CSV_PATH)

print(f"Dataset carregado com sucesso!")
print(f"Total de registros: {len(df)}")

# ==========================================
# Preparação dos dados
# ==========================================

df["datetime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"]
)

df["day"] = df["datetime"].dt.day_name()
df["month"] = df["datetime"].dt.month_name()
df["hour"] = df["datetime"].dt.hour

# ==========================================
# Corridas por dia da semana
# ==========================================

top_dias = df["day"].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_dias.values,
    y=top_dias.index,
    palette="Set2"
)

plt.title("Top dias da semana")
plt.xlabel("Quantidade de Corridas")
plt.ylabel("Dia da Semana")

plt.savefig(
    os.path.join(VIS_DIR, "top_dias.png")
)

plt.show()

# ==========================================
# Corridas por mês
# ==========================================

top_meses = df["month"].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_meses.values,
    y=top_meses.index,
    palette="Set3"
)

plt.title("Top meses")
plt.xlabel("Quantidade de Corridas")
plt.ylabel("Mês")

plt.savefig(
    os.path.join(VIS_DIR, "top_meses.png")
)

plt.show()

# ==========================================
# Corridas por hora
# ==========================================

top_horas = df["hour"].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_horas.index,
    y=top_horas.values,
    palette="viridis"
)

plt.title("Top 10 horários com mais corridas")
plt.xlabel("Hora")
plt.ylabel("Quantidade")

plt.savefig(
    os.path.join(VIS_DIR, "top_horas.png")
)

plt.show()

# ==========================================
# Status das corridas
# ==========================================

if "Booking Status" in df.columns:

    top_status = (
        df["Booking Status"]
        .value_counts()
        .nlargest(10)
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_status.values,
        y=top_status.index,
        palette="Set2"
    )

    plt.title("Top 10 status das corridas")

    plt.savefig(
        os.path.join(VIS_DIR, "top10_status_bar.png")
    )

    plt.show()

# ==========================================
# Percentual dos status
# ==========================================

if "Booking Status" in df.columns:

    top_status = (
        df["Booking Status"]
        .value_counts()
        .nlargest(10)
    )

    plt.figure(figsize=(8, 8))

    plt.pie(
        top_status,
        labels=top_status.index,
        autopct="%1.1f%%",
        colors=sns.color_palette("Set2")
    )

    plt.title(
        "Percentual dos Top 10 status das corridas"
    )

    plt.savefig(
        os.path.join(VIS_DIR, "top10_status_pie.png")
    )

    plt.show()

# ==========================================
# Distribuição dos preços
# ==========================================

if "Booking Value" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Booking Value"],
        bins=30,
        kde=True,
        color="skyblue"
    )

    plt.title("Distribuição dos preços das corridas")

    plt.savefig(
        os.path.join(
            VIS_DIR,
            "distribuicao_precos.png"
        )
    )

    plt.show()

    plt.figure(figsize=(8, 6))

    sns.boxplot(
        x=df["Booking Value"],
        color="lightgreen"
    )

    plt.title(
        "Boxplot dos preços das corridas"
    )

    plt.savefig(
        os.path.join(
            VIS_DIR,
            "boxplot_precos.png"
        )
    )

    plt.show()

# ==========================================
# Top origens
# ==========================================

if "Pickup Location" in df.columns:

    top_origens = (
        df["Pickup Location"]
        .value_counts()
        .nlargest(10)
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_origens.values,
        y=top_origens.index,
        palette="Set2"
    )

    plt.title(
        "Top 10 origens das corridas"
    )

    plt.savefig(
        os.path.join(
            VIS_DIR,
            "top10_origens.png"
        )
    )

    plt.show()

# ==========================================
# Top destinos
# ==========================================

if "Drop Location" in df.columns:

    top_destinos = (
        df["Drop Location"]
        .value_counts()
        .nlargest(10)
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_destinos.values,
        y=top_destinos.index,
        palette="Set3"
    )

    plt.title(
        "Top 10 destinos das corridas"
    )

    plt.savefig(
        os.path.join(
            VIS_DIR,
            "top10_destinos.png"
        )
    )

    plt.show()

# ==========================================
# Série temporal
# ==========================================

corridas_por_dia = (
    df.groupby(
        df["datetime"].dt.date
    ).size()
)

top_corridas = (
    corridas_por_dia.nlargest(10)
)

plt.figure(figsize=(12, 6))

top_corridas.plot(
    kind="bar",
    color="steelblue"
)

plt.title(
    "Top 10 dias com mais corridas"
)

plt.savefig(
    os.path.join(
        VIS_DIR,
        "top10_dias_corridas.png"
    )
)

plt.show()

# ==========================================
# Finalização
# ==========================================

print("\n✅ Análises concluídas!")

print(f"\nGráficos salvos em:\n{VIS_DIR}")

print("\nArquivos gerados:\n")

for arquivo in sorted(os.listdir(VIS_DIR)):
    print(f"- {arquivo}")