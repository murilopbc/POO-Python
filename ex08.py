class Estudante:
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota

    def calcular_nota(self):
        if self.nota >= 7:
            print(f"O aluno(a) {self.nome} foi aprovado na disciplina de Matemática. Sua nota final é {self.nota:.2f}")
        else:
            print(f"{self.nome}, sua nota na disciplina de matemática foi {self.nota:.2f}, então você reprovou!")
