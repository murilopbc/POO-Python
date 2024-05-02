class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, eu sou {self.nome}!"

    def trabalhar(self):
        print("Pessoa trabalhando de forma genérica")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def exibir_informacoes(self):
        return f"{self.nome} tem {self.idade} anos e trabalha como {self.cargo}."

    def trabalhar(self):
        print(f"Funcionário trabalhando no cargo {self.cargo}")

# Criando instâncias
pessoa1 = Pessoa(nome="João", idade=25)
funcionario1 = Funcionario(nome="Ana", idade=35, cargo="Engenheira")

# Chamando o método trabalhar de cada instância
pessoa1.trabalhar()       # Saída: Pessoa trabalhando de forma genérica
funcionario1.trabalhar()  # Saída: Funcionário trabalhando no cargo Engenheira
