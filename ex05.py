class Carro:
    def __init__(self, velocidade: float):
        self.velocidade = velocidade

    def a(self):
        a = self.velocidade + 10
        print(f"Se eu acelerar, minha velocidade será {a:.2f} km/h")

    def f(self):
        f = self.velocidade - 10
        print(f"Se eu frear, minha velocidade será {f:.2f} km/h")

