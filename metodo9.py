from ex09 import ContaBancaria

saldo_inicial = ContaBancaria()

while True:
    print("O que deseja realizar?:\n1-Sacar\n2-Depositar\n3-Verificar Saldo\n4-Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        valor = float(input("Informe o valor do saque: "))
        saldo_inicial.sacar(valor)
    elif opcao == 2:
        valor = float(input("Informe o valor do déposito: "))
        saldo_inicial.depositar(valor)
    elif opcao == 3:
        print(f"Seu saldo atual é R$ {saldo_inicial.saldo}")
    elif opcao == 4:
        print("Saindo do programa em instantes!")
        break
    else:
        print("Opção Inválida!")
