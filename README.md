# Análise de Dados Ecoloop

Este projeto realiza uma análise automatizada dos dados de depósitos e pontos das máquinas Ecoloop.

## Como foi realizado

### Ferramenta usada
- Python com biblioteca pandas para análise de dados

### Processo
1. Leitura do arquivo Excel com os dados das máquinas
2. Análise automática usando funções do pandas:
   - `value_counts()` para contar depósitos por máquina
   - `sum()` para calcular o total de pontos

### Resultados

#### Depósitos por máquina:
- Máquina 97: 30 depósitos
- Máquina 123: 25 depósitos
- Máquina 100: 21 depósitos
- Máquina 94: 20 depósitos
- Máquina 106: 2 depósitos
- Máquinas 119 e 126: 1 depósito cada

#### Total de pontos: 635 pontos

### Vantagens
- Processamento rápido
- Código simples
- Resultados precisos
- Fácil de modificar

A solução é eficiente porque automatiza a análise e fornece resultados confiáveis de forma rápida. 