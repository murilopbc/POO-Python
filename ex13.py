class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def exibir_info(self):
        return f"{self.nome} tem {self.idade} anos e trabalha como {self.cargo}"


funcionario1 = Funcionario(nome="Murilo", idade=35, cargo="Programador")

infoFuncionario = funcionario1.exibir_info()
print(infoFuncionario)
