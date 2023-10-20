class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito efetuado com sucesso!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque concluído com sucesso!")
        else:
            print("Saldo insuficiente!")
