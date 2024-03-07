class Cliente:

    def __init__(self, nome, email, idade) -> None:
        self.nome = nome
        self.email = email
        self.idade = idade

    def exibir(self):
        print(self.nome, self.email, self.idade)

guilherme = Cliente("Guilherme", "email@email.com", "20")

print(guilherme.nome)
print(guilherme.email)
print(guilherme.idade)