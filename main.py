
class Circulo:
    def __init__(self, raio: float):
        self.raio = raio

    def area(self):
        area = 3.14 * (self.raio * self.raio)
        print(f"A área do círculo é {area:.2f}")
