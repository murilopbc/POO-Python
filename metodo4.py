from ex04 import Livro

titulo = input("Digite o nome do livro: ")
autor = input("Digite o nome do autor(a): ")

resumo = Livro(titulo, autor)
resumo.book()
