— Projeto Uber: Análise Exploratória de Dados
1. Introdução
Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (AED) utilizando o conjunto de dados “Uber Ride Analytics Dashboard”, disponibilizado no Kaggle. A análise busca compreender padrões de uso do serviço de transporte por aplicativo, identificar horários de maior demanda, avaliar características das corridas e explorar relações entre variáveis como distância, valor da corrida, tipo de veículo e status da viagem.
A AED é uma etapa fundamental em projetos de Ciência de Dados e Inteligência Artificial, pois permite conhecer profundamente o conjunto de dados antes de aplicar modelos de aprendizado de máquina. A partir das informações extraídas, torna‑se possível propor aplicações futuras, como previsão de preço, classificação de status de corrida ou análise de comportamento de usuários.
---------------------------------------

# Análise Exploratória de Dados - Uber Ride Analytics

## Introdução
Este projeto realiza uma análise exploratória de dados (AED) utilizando o dataset **Uber Ride Analytics Dashboard**, disponível no Kaggle. O objetivo é compreender padrões de utilização do serviço de transporte por aplicativo, variações temporais e características das corridas realizadas no estado de Santa Catarina.

A AED é uma etapa fundamental para identificar variáveis relevantes e padrões de comportamento, servindo como base para futuras aplicações em modelos de Inteligência Artificial, como classificação e regressão.

---

## Etapas do Projeto

1. **Coleta de dados**  
   - Dataset obtido do Kaggle: `ncr_ride_bookings.csv`.

2. **Limpeza e organização**  
   - Conversão de colunas de data e hora em formato `datetime`.  
   - Criação de variáveis derivadas: dia da semana, mês e hora.  
   - Estruturação das colunas relevantes: origem, destino, valor da corrida, status.

3. **Análise Exploratória de Dados (AED)**  
   Foram gerados gráficos para explorar os principais aspectos do dataset:
   - Corridas por dia da semana (Top 10).  
   - Corridas por mês (Top 10).  
   - Corridas por hora do dia (Top 10).  
   - Status das corridas (Top 10 em barras e percentual em pizza).  
   - Distribuição dos preços (histograma e boxplot).  
   - Origem das corridas (Top 10 locais).  
   - Destino das corridas (Top 10 locais).  
   - Série temporal (Top 10 dias com mais corridas).

---

## Principais Insights

- **Padrões temporais**:  

  A maior concentração de corridas ocorre em dias úteis e nos horários de pico (manhã e fim da tarde).

- **Distribuição de preços**: 
 
  A maioria das corridas se concentra em faixas médias de valor, com alguns outliers de corridas muito caras.

- **Origem e destino**:  

  Os locais mais frequentes de origem e destino estão concentrados em regiões centrais, indicando maior demanda nessas áreas.

- **Status das corridas**:  

  A maioria das corridas foi concluída, mas há uma proporção significativa de cancelamentos por clientes e motoristas.

- **Série temporal**:  

  Alguns dias específicos apresentam picos de demanda, possivelmente relacionados a eventos ou sazonalidade.

---

## Aplicações Futuras em Inteligência Artificial

Com base nos padrões identificados, este dataset pode ser utilizado em tarefas de IA como:

- **Classificação**:  

  Prever se uma corrida será concluída ou cancelada com base em variáveis como horário, origem, destino e tipo de veículo.

- **Regressão**:  

  Estimar o valor da corrida considerando distância, localização e horário.

- **Análise preditiva**:  

  Identificar períodos de maior demanda para otimizar a alocação de motoristas.

---

## Estrutura da Entrega

O arquivo compactado contém:

- Código-fonte em Python (`.ipynb` ou `.py`).  
- Dataset utilizado (`ncr_ride_bookings.csv`).  
- Pasta `visualizacoes` com todos os gráficos gerados em `.png`.  
- Este arquivo de documentação (`README.md`).  

---

## Conclusão

A análise exploratória permitiu compreender os principais padrões de utilização do serviço de transporte por aplicativo em Santa Catarina. Esses resultados fornecem uma base sólida para futuras aplicações de Inteligência Artificial, contribuindo para otimizar a mobilidade urbana e melhorar a experiência dos usuários.
