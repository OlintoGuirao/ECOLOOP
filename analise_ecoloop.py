import pandas as pd

try:
    # Lendo o arquivo Excel com as colunas específicas
    df = pd.read_excel('Análise de Dados.xlsx', usecols=['ID MÁQUINA', 'DATA HORA', 'PONTOS'])
    
    # Análise dos depósitos por máquina
    print("\nQuantidade de depósitos por máquina:")
    depositos_por_maquina = df['ID MÁQUINA'].value_counts()
    for maquina, quantidade in depositos_por_maquina.items():
        print(f"Máquina {maquina}: {quantidade} depósitos")

    # Total de pontos distribuídos
    total_pontos = df['PONTOS'].sum()
    print(f"\nTotal de pontos distribuídos: {total_pontos} pontos")
    
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}") 