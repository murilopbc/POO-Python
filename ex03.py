class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def print(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos ")
