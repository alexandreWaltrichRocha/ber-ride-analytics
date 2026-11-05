# ============================
# 0. Importação de bibliotecas e configuração
# ============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

os.makedirs('./visualizacoes', exist_ok=True)

# ============================
# 1. Carregamento do dataset
# ============================
df = pd.read_csv('../data/ncr_ride_bookings.csv')

df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
df['day'] = df['datetime'].dt.day_name()
df['month'] = df['datetime'].dt.month_name()
df['hour'] = df['datetime'].dt.hour

# ============================
# 2. Corridas por dia da semana (Top 10)
# ============================
top_dias = df['day'].value_counts().nlargest(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_dias.values, y=top_dias.index, palette="Set2")
plt.title("Top dias da semana")
plt.savefig('./visualizacoes/top_dias.png')
plt.show()

# ============================
# 3. Corridas por mês (Top 10)
# ============================
top_meses = df['month'].value_counts().nlargest(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_meses.values, y=top_meses.index, palette="Set3")
plt.title("Top meses")
plt.savefig('./visualizacoes/top_meses.png')
plt.show()

# ============================
# 4. Corridas por hora (Top 10)
# ============================
top_horas = df['hour'].value_counts().nlargest(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_horas.index, y=top_horas.values, palette="viridis")
plt.title("Top 10 horários com mais corridas")
plt.savefig('./visualizacoes/top_horas.png')
plt.show()

# ============================
# 5. Status das corridas (Top 10 em barras)
# ============================
if 'Booking Status' in df.columns:
    top_status = df['Booking Status'].value_counts().nlargest(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_status.values, y=top_status.index, palette="Set2")
    plt.title("Top 10 status das corridas")
    plt.savefig('./visualizacoes/top10_status_bar.png')
    plt.show()

# ============================
# 6. Percentual de status (Top 10 em pizza)
# ============================
if 'Booking Status' in df.columns:
    top_status = df['Booking Status'].value_counts().nlargest(10)
    plt.figure(figsize=(8,8))
    plt.pie(top_status, labels=top_status.index, autopct='%1.1f%%', colors=sns.color_palette("Set2"))
    plt.title("Percentual dos Top 10 status das corridas")
    plt.savefig('./visualizacoes/top10_status_pie.png')
    plt.show()

# ============================
# 7. Distribuição de preços
# ============================
if 'Booking Value' in df.columns:
    plt.figure(figsize=(10,6))
    sns.histplot(df['Booking Value'], bins=30, kde=True, color="skyblue")
    plt.title("Distribuição dos preços das corridas")
    plt.savefig('./visualizacoes/distribuicao_precos.png')
    plt.show()

    plt.figure(figsize=(8,6))
    sns.boxplot(x=df['Booking Value'], color="lightgreen")
    plt.title("Boxplot dos preços das corridas")
    plt.savefig('./visualizacoes/boxplot_precos.png')
    plt.show()

# ============================
# 8. Origem das corridas (Top 10)
# ============================
if 'Pickup Location' in df.columns:
    top_origens = df['Pickup Location'].value_counts().nlargest(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_origens.values, y=top_origens.index, palette="Set2")
    plt.title("Top 10 origens das corridas")
    plt.savefig('./visualizacoes/top10_origens.png')
    plt.show()

# ============================
# 9. Destino das corridas (Top 10)
# ============================
if 'Drop Location' in df.columns:
    top_destinos = df['Drop Location'].value_counts().nlargest(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_destinos.values, y=top_destinos.index, palette="Set3")
    plt.title("Top 10 destinos das corridas")
    plt.savefig('./visualizacoes/top10_destinos.png')
    plt.show()

# ============================
# 10. Série temporal (Top 10 dias com mais corridas)
# ============================
corridas_por_dia = df.groupby(df['datetime'].dt.date).size()
top_corridas = corridas_por_dia.nlargest(10)
plt.figure(figsize=(12,6))
top_corridas.plot(kind='bar', color="steelblue")
plt.title("Top 10 dias com mais corridas")
plt.savefig('./visualizacoes/top10_dias_corridas.png')
plt.show()

print("✅ Todas as análises foram geradas e salvas em ./visualizacoes")



import os

print(os.listdir('./visualizacoes'))


