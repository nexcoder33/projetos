import os

op = 2

while op == 2:

    os.system("clear")

#obetendo valores

    nome = input("Digite seu nome: ")
    valor = (int(input("Digite o valor bruto: ")))
    despesa = (int(input("Digite a despesa: ")))
    total = valor - despesa

#mostrando valores

    os.system("clear")

    print("Ola ", nome, "!", "\n\nValor Disponivel: ", valor, "\nDespesa: ", despesa, "\nRestante: ", total)
    print("_____________________________________")
    op = (int(input("1 - Sair: \n2 - Repetir: ")))