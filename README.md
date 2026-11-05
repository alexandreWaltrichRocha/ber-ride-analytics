# 🚕 BER Ride Analytics

Projeto de análise de dados de mobilidade urbana desenvolvido utilizando Python, Pandas, Seaborn, Matplotlib e Streamlit.

O objetivo é identificar padrões de utilização de corridas por meio de análises exploratórias, visualizações de dados e um dashboard interativo.

---

# 📌 Objetivos

O projeto busca responder perguntas como:

- Quais são os horários de pico?
- Quais dias possuem maior volume de corridas?
- Como os preços das corridas estão distribuídos?
- Quais são os principais pontos de origem?
- Quais são os principais destinos?
- Qual a distribuição dos status das corridas?
- Como o comportamento das corridas varia ao longo do tempo?

---

# 🛠 Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

# 📁 Estrutura do Projeto

```text
ber-ride-analytics/
├── app.py
├── data/
│   └── ncr_ride_bookings.csv
├── notebooks/
│   └── ber_ride_analytics.py
├── visualizacao/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

Arquivo utilizado:

```text
data/ncr_ride_bookings.csv
```

Quantidade de registros analisados:

```text
150.000 corridas
```

---

# 🔍 Análises Realizadas

- Corridas por dia da semana
- Corridas por mês
- Corridas por hora
- Distribuição dos preços
- Boxplot dos preços
- Análise dos status das corridas
- Top 10 origens
- Top 10 destinos
- Série temporal das corridas

---

# 📈 Dashboard Interativo

O projeto possui um dashboard em Streamlit com:

✅ Indicadores (KPIs)

✅ Filtro por Status da Corrida

✅ Filtro por Tipo de Veículo

✅ Corridas por Hora

✅ Corridas por Dia da Semana

✅ Distribuição dos Status

✅ Top 10 Destinos

✅ Top 10 Origens

✅ Distribuição dos Preços

✅ Tabela Interativa

---

# ▶️ Como Executar

## 1. Clonar o repositório

```bash
git clone https://github.com/alexandreWaltrichRocha/ber-ride-analytics.git
```

## 2. Entrar na pasta

```bash
cd ber-ride-analytics
```

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 🐍 Executar Análise Python

```bash
python notebooks/ber_ride_analytics.py
```

Os gráficos serão gerados automaticamente na pasta:

```text
visualizacao/
```

---

# 🚀 Executar Dashboard Streamlit

```bash
python -m streamlit run app.py
```

Depois abra:

```text
http://localhost:8501
```

---

# 📊 Principais Insights

A análise permite identificar:

- Horários de maior demanda
- Dias mais movimentados
- Principais destinos das corridas
- Principais origens das corridas
- Distribuição dos preços
- Padrões operacionais através dos status das corridas

---

# 🎯 Resultados

O projeto gera automaticamente:

- Indicadores de desempenho
- Gráficos interativos
- Visualizações exploratórias
- Dashboard de acompanhamento
- Análises de mobilidade urbana

---

# 👨‍💻 Autor

**Alexandre Waltrich Rocha**

GitHub:
https://github.com/alexandreWaltrichRocha

---

# ⭐ Próximas Melhorias

- Publicação do dashboard na Streamlit Cloud
- Inclusão de mapas interativos
- KPIs avançados
- Comparações por período
- Análise geográfica das corridas
- Exportação de relatórios