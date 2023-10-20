from ex03 import Pessoa

nome = input("Digite o seu nome:  ")
idade = int(input("Digite sua idade: "))

apresentar = Pessoa(nome, idade)
apresentar.print()
