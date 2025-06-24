#ESTRUTURAS CONDICIONAIS E DE REPRETIÇÃO
#Obs.: indentação em python é obrigatória (1 Tab = 4 espaços)


#---ESTRUTURA CONDICIONAL (IF, ELIF, ELSE)
import sys

saldo = 2000.0
opcao = int(input("Informe uma opção: /n[1] Sacar /n[2] Extrato /n -> "))

if opcao == 1:
    saque = float(input("Informe o valordo saque: "))

    if saldo >= saque:
        print("Realizando saque...")
        saldo -= saque

    else:
        print("Saldo insuficiente!")

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    sys.exit("Opção inválida")


#---IF TERNÁRIO
#permite escrever condição em uma única linha
#composto por 3 partes:
#   1ª Retorno caso a espressão retorne verdadeira
#   2ª Expressão Lógica
#   3ª Retorno caso a expressão não seja atendida

saque = 1002
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")


#---ESTRUTURAS DE REPETIÇÃO
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()

for numero in range(0, 11, 3): #(núm mín, núm máx, intervalor entre os números)
    print(numero, end="")

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar /n[2] Extrato /n[0] Sair/n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao ==2:
        print("Exibindo o extrato...")


#---BREAK e CONTINUE
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

for numero in range(20):
    if numero == 5:
        continue

    if numero == 12:
        break

    print(numero, end=" ")
