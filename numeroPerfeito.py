import math

def eh_numero_perfeito(n):
    soma_divisores = 1  # Começa com 1, pois 1 é divisor de qualquer número
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            soma_divisores += i
            if i != n // i:  # Evitar adicionar o mesmo divisor duas vezes
                soma_divisores += n // i
    return soma_divisores == n

def encontrar_numeros_perfeitos(limite):
    numeros_perfeitos = []
    for num in range(2, limite + 1):
        if eh_numero_perfeito(num):
            numeros_perfeitos.append(num)
    return numeros_perfeitos

# Definir o limite para procurar números perfeitos
limite = int(input("Digite o limite para encontrar números perfeitos: "))

# Encontrar e exibir os números perfeitos
numeros_perfeitos = encontrar_numeros_perfeitos(limite)
print(f"Números perfeitos até {limite}: {numeros_perfeitos}")
