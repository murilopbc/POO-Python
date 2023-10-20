class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        return num1 / num2


num1 = float(input("Digite um número: "))
num2 = float(input("Digite um outro número: "))

operacoes = Calculadora()

resultado_soma = operacoes.somar(num1, num2)
print(f"A soma dos números é {resultado_soma:.2f}")

resultado_subtracao = operacoes.subtrair(num1, num2)
print(f"A subtração dos números é {resultado_subtracao:.2f}")

resultado_multiplicacao = operacoes.multiplicar(num1, num2)
print(f"A multiplicação dos números é {resultado_multiplicacao:.2f}")

resultado_dividir = operacoes.dividir(num1, num2)
print(f"A divisão dos números é {resultado_dividir:.2f}")
