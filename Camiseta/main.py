class Camiseta:
    def __init__(self, marca: str, cor: str, tamanho: str, preco: float):
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def promo(self):

        if self.preco >= 100:
            self.preco = self.preco * 0.9
            print("O valor da camiseta com desconto é R$", self.preco)
        else:
            self.preco = self.preco * 0.95
            print("O valor da camiseta com desconto é R$", self.preco)
