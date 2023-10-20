class Caneta:
    def __init__(self, cor: str, marca: str):
        self.cor = cor
        self.marca = marca

    def pen(self):
        print(f"A caneta {self.cor} é da marca {self.marca}")
