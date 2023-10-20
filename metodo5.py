from ex05 import Carro

try:
    speed = float(input("Digite sua velocidade: "))
    if speed > 0:
        acelerar = Carro(speed)
        frear = Carro(speed)
        acelerar.a()
        frear.f()
    else:
        print("Valor Inválido!")
except:
    print("")
