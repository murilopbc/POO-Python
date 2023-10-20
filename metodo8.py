from ex08 import Estudante

nome = input("Digite o seu nome: ")
nota = float(input("Digite sua nota: "))

aprovado = Estudante(nome, nota)
aprovado.calcular_nota()
