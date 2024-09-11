# Este programa calcula o percentual de representação que cada estado teve dentro do valor total mensal de uma distribuidora.  


# Dados de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o valor total de faturamento
total = sum(faturamento_estados.values())

# Calcula o percentual de representação de cada estado
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}

# Exibe os resultados
print(f"Valor total de faturamento: R${total:.2f}")
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
