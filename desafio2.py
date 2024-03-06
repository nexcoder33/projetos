# Numero digitado pelo usuário
numero = int(input("Digite um numero: "))
primos = []

# Função para identificar números primos
def identificador(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Percorre números e identifica primos
for x in range(2, numero + 1):
    if identificador(x):
        primos.append(x)

# Exibe lista de números primos
print(f"Números primos até {numero}: {primos}")
