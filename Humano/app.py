from main import Humano

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
rg = int(input("Digite seu RG:"))
cpf = int(input("Digite seu CPF: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

human1 = Humano(nome, idade, rg, cpf, altura, peso)

human1.imc()
human1.age()
