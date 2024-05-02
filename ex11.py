# CLASSE PESSOA COM ATRIBUTO NOME E IDADE
class Pessoa:
    total_pessoas = 0  # atributo estático

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self._idade = idade
        Pessoa.total_pessoas += 1

    # MÉTODO CUMPRIMENTAR

    def cumprimentar(self):
        return f"Olá {self.nome}!"

    @staticmethod
    def get_total_pessoas():
        return Pessoa.total_pessoas

    def __str__(self):
        return f"Meu nome é {self.nome} e tenho {self._idade} anos"


# CRIAÇÃO DO OBJETO


pessoa1 = Pessoa(nome="Murilo", idade=18)
pessoa2 = Pessoa(nome="João", idade=17)
pessoa3 = Pessoa(nome="Murilo", idade=18)
pessoa4 = Pessoa(nome="João", idade=17)
pessoa5 = Pessoa(nome="Murilo", idade=18)
pessoa6 = Pessoa(nome="João", idade=17)


# CHAMAR O OBJETO

print(pessoa1)
print(pessoa2)

# obtendo e exibindo o total de pessoas

total_pessoas = Pessoa.get_total_pessoas()
print(f"Total de pessoas: {total_pessoas}")
