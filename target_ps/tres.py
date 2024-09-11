''' Este programa calcula, a partir de um arquivo JSON com faturamentos diários de uma empresa:
 - O menor e o maior valor de faturamento ocorrido em um dia do mês;
 - Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.'''


import json

# Função para carregar dados do JSON
def carregar_dados(arq):
    with open(arq, 'r') as file:
        dados = json.load(file)
    return dados

# Função para calcular o menor e maior faturamento e o número de dias acima da média
def analise(dados):
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    if not faturamentos:
        return None, None, 0  # Caso não haja faturamento
    
    menor = min(faturamentos)
    maior = max(faturamentos)
    
    media = sum(faturamentos) / len(faturamentos)
    
    dias = sum(1 for valor in faturamentos if valor > media)
    
    return menor, maior, dias

# Arquivo JSON com os dados de faturamento
arq = 'faturamento.json'

# Carregar dados
dados = carregar_dados(arq)

# Analisar faturamento
menor, maior, dias = analise(dados)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias}")
