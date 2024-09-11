# Este programa inverte uma string inserida pelo usuário

def inverter(s):
    # Inicializa uma string vazia para armazenar o resultado
    resultado = ""
    
    # Itera sobre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

# Execução da função
print("String invertida:", inverter(input()))
