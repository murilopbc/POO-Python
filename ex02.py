class Retangulo:
    def __init__(self, altura: float, largura: float):
        self.altura = altura
        self.largura = largura

    def p(self):
        p = (self.altura + self.largura) * 2
        print(f"O perímetro do retângulo é {p:.2f}")
