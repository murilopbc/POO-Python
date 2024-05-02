class Humano:

    def __init__(self, nome: str, idade: int, rg: int, cpf: int, altura: float, peso: float):
        self.__nome = nome
        self.__idade = idade
        self.__rg = rg
        self.__cpf = cpf
        self.altura = altura
        self.peso = peso

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        self.__idade = nova_idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def imc(self):
        imc = self.peso / (self.altura * self.altura)
        print(f"Seu imc é {imc:.2f}")

    def age(self):
        if self.idade < 12:
            print("Você é uma criança!")
        elif self.idade < 18:
            print("Você é Jovem!")
        elif self.idade < 60:
            print("Você é um adulto!")
        else:
            print("Você é um idoso")
