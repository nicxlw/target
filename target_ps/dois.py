# Este programa calcula a sequência de Fibonacci e informa se um número informado pelo usuário faz parte dela

# Função para calcular a sequência de Fibonacci até um determinado número
def fib(n):

     # Defesa do codigo
    try:
        if '.' in n: # Se o usuario digitar um float, gera um erro
            raise ValueError
        n = int(n) # Se o usuario digitar uma entrada nao numerica, gera um erro
    except ValueError:
        return f"Entrada inválida"
    
    n = int(n) # Converte a entrada para inteiro
    a, b = 0, 1 # Dois primeiros números da sequência
    
    # Verifica se o número informado é 0 ou 1 para evitar cálculo desnecessário
    if n == 0 or n == 1:
        return f"O número {n} pertence à sequência de Fibonacci."
    
    # Calcula a sequência até que b seja maior ou igual ao número informado
    while b <= n:
        if b == n:
            return f"O número {n} pertence à sequência de Fibonacci."
        a = b
        b = a + b
        
    return f"O número {n} não pertence à sequência de Fibonacci."

# Execução da função
print(fib(input("Digite um número inteiro:")))

