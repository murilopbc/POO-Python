from main import Camiseta


marca = input("Digite a marca da sua camiseta: ")
cor = input("Qual a cor da sua camiseta: ")
tamanho = input("Qual o tamanho da sua camiseta: ")
valorTotal = float(input("Digite o preço da sua camiseta: "))

compra1 = Camiseta(marca, cor, tamanho, valorTotal)

compra1.promo()
