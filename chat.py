import os

#programa mensagem

nome = (input("Digite seu nome: "))
mensagens = []


while True:

    #limpar terminal
    os.system('clear')

    #verficar se ja tem dados

    if len(mensagens) > 0:
        for m in mensagens:
            print(m["nome"], " - ", m["texto"])

        print("______________________________")

    #obter texto

    texto = input("mensagem: ")
    if texto == "fim":
        break

    #adicionando texto

    mensagens.append({
        "nome":nome,
        "texto":texto
    })