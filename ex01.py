# CLASSE PESSOA COM ATRIBUTO NOME E IDADE
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
# MÉTODO CUMPRIMENTAR

    def cumprimentar(self):
        return f"Olá {self.nome}!"

    def __str__(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos"

# CRIAÇÃO DO OBJETO


pessoa1 = Pessoa(nome="Murilo", idade=18)
pessoa2 = Pessoa(nome="João", idade=17)

# CHAMAR O OBJETO

print(pessoa1)
print(pessoa2)
