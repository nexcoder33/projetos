#calcular fatorial

valor = int(input("Digite um numero: "))

#calcular

def calcular(n):
    if n == 0 or n == 1:
        return n
    else: return n * calcular(n - 1)

print(calcular(valor))