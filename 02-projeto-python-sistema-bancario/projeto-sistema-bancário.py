#PROJETO PRÁTICO DE PYTHON
#O objetivo é criar um sistema bancário com operações básicas: sacar, depositar e visualizar extrato

#   v1 de teste - trabalhando apenas com 1 usuário
#limite de 3 saques diários, de até R$ 500 cada
#mensagem personalizada para falta de saldo
#todo depósito e todo saque devem ser armazenados em variável e exibidos na operação extrato
#no fim da lista do extrato deve ser exibido o saldo atual da conta
#formato dos valores: R$ xxx.xx


menu = """
      ============================
      
        Informe a ação desejada:
      
        1 - Depositar
        2 - Sacar
        3 - Consultar extrato
        0 - Sair

      ============================

      --> 
      """

saldo = 0
limite = 500
qtdd_saque = 0
LIMITE_SAQUE = 3
extrato = ""

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\nDepositar")
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito:      R$ {valor:.2f}\n"
            print("Depósito efetuado com sucesso!")
        else:
            print("Valor inválido! Tente novamente")

    elif opcao == "2":
        print("\nSacar")
        valor = float(input("Digite o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = qtdd_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Falha! Saldo insuficiente. \nTente novamente")

        elif excedeu_limite:
            print("Falha! Valor acima do limite permitido. \nTente novamente")

        elif excedeu_saque:
            print("Falha! Limite diário de saques atingido. \nTente novamente")

        else:
            saldo -= valor
            print("Saque efetuado com sucesso!")
            extrato += f"Saque:         R$ {valor:.2f}\n"
            qtdd_saque += 1

    elif opcao == "3":
        print("\nConsultar extrato")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"\nSALDO ATUAL    R$ {saldo:.2f}")

    elif opcao == "0":
        print("Até a próxima! \nEncerrando...")
        break

    else:
        print("\nOpção inválida. Tente novamente --> ")
