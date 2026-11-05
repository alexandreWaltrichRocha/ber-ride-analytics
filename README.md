# BER Ride Analytics

Projeto de análise de dados de mobilidade urbana desenvolvido utilizando Python.

## Objetivo

O projeto busca identificar padrões de utilização de corridas por meio de análises exploratórias e visualizações de dados.

As análises incluem:

- Dias com maior volume de corridas
- Horários de pico
- Meses mais movimentados
- Distribuição dos preços
- Status das corridas
- Principais origens
- Principais destinos

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn

## Estrutura do Projeto

```text
ber-ride-analytics/
├── data/
│   └── ncr_ride_bookings.csv
├── notebooks/
│   └── ber_ride_analytics.py
├── visualizacao/
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset

Arquivo utilizado:

```text
data/ncr_ride_bookings.csv
```

Total de registros analisados:

```text
150.000 corridas
```

## Análises Realizadas

- Corridas por dia da semana
- Corridas por mês
- Corridas por hora
- Status das corridas
- Distribuição dos preços
- Boxplot dos preços
- Top 10 origens
- Top 10 destinos
- Série temporal das corridas

## Como Executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python notebooks/ber_ride_analytics.py
```

## Resultados

O projeto gera automaticamente gráficos na pasta:

```text
visualizacao/
```

Incluindo:

- Top dias da semana
- Top meses
- Top horários
- Distribuição dos preços
- Status das corridas
- Principais origens
- Principais destinos

## Autor

Alexandre Waltrich Rocha
