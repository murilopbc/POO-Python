class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def book(self):
        print(f"O livro {self.titulo} foi escrito pelo autor(a) {self.autor}")
