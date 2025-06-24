print("Hello world!")

# Modo interativo
# dir()   e   help()


#---VARIÁVEIS
age, name = (26, 'Gabriela')    
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

name = input("Informe seu nome: ")
print(f'Meu nome é {name}')


#---CONSTANTES
RG = 1230032145     #nome da variável todo em maiúsculo
ABS_PATH = '/home/chaplin/Bootcamp Santander Backend com Python'
BRAZILIAN_STATES = ['SP', 'RJ', 'MG', 'SC', 'RS',]
print(BRAZILIAN_STATES)


#---CONVERSÃO DE VARIÁVEIS
numero_inteiro = 10
preco_quebrado = float(numero_inteiro) #pra converter tipo, pode-se usar o comando, como int() ou string() etc
print(preco_quebrado)
preco_quebrado = numero_inteiro/4      #dependendo da operação, ela vai converter automaticamente
print(preco_quebrado)

#a conversão nem sempre é possível:
preco = 'python'
print(preco)
#print(float(preco))   DÁ ERRO

valor = '20'
print(float(valor))


#---OPERADORES ARITMÉTICOS
print(2+7)
print(numero_inteiro/2)     #a divisão converte pra float, mesmo que o resultado não fique quebrado
print(numero_inteiro//2)    #com barra dupla o resultado vai pra inteiro, caso o resultado seja quebrado, ele arredonda
print(numero_inteiro//4)
print(10%3)                 #módulo (resto de uma divisão)
print(2**3)                 #exponenciação (2*2*2)

str(numero_inteiro)

numero_escrito = f'o resultado é {numero_inteiro}'
print(numero_escrito)

#precedência para operações em python segue a convensão matemática:
# parêntesis > expoêntes > multiplicação > divisão (esquerda para a direita) soma > subtração (esquerda para a direita)

# (10 - 5 * 2)      = 0
# ((10 - 5) * 2)    = 10
# (10 ** 2 * 2)     = 200
# (10 ** (2 * 2))   = 10000
# (10 / 2 * 4)      = 20.0


#---OPERADORES DE COMPARAÇÃO
print(450 == 200)   #False
print(450 != 200)   #True
print(450 < 200)    #False
print(450 >= 200)   #True


#---OPERADORES DE ATRIBUIÇÃO p/ definir valor inicial ou sobrescrever valor da var
saldo = 500
saldo += 200        #adiciona o valor ao "saldo" que já havia antes -> saldo = saldo + 200
saldo *= 2
saldo //=2
saldo %= 2


#---OPERADORES LÓGICOS
saldo = 300
saque = 200
limite = 100
conta_especial = True
contatos_emergencia = []

print(saldo >= saque and saque <= limite)   #False
print(saldo >= saque or saque <= limite)    #True

#operador Negação
not 1000 > 1500             #um "not" falso é True; é o inverso
not contatos_emergencia     #True; lista vazia é False, com o not seria "não Falso"

#precedência na operação lógica
saldo >= saque and saque <= limite or conta_especial and saldo >= saque     #True
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(True and True)    #True
print(False and False)  #False
print(True or False)    #True
print(True and False)   #False
print(False or False)   #False


#---OPERADORES DE IDENTIDADE
#compara se dois objetos ocupam a mesma posição na memória
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso     #True, ocupam o mesmo lugar, pois é o mesmo valor (recebe o valor da outra variável)
curso is not nome_curso #False
saldo is limite         #True


#---OPERADORES DE ASSOCIAÇÃO
#verificam se um objeto está presente em uma sequência
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso       #True (lembrando que Python é case sensitive)
"maça" not in frutas    #True
200 in saques           #False


#---BUILTINS input() e print()
nome = "Gabriela"
sobrenome = "Chaplin"

print(nome, sobrenome)              #por padrão, o separador é um espaço em branco              >>> Gabriela Chaplin
print(nome, sobrenome, end="...\n") #add reticências no final e /n insere uma troca de linha    >>> Gabriela Chaplin...
print(nome, sobrenome, sep="#")     #insere o sep em todos os espaços entre o que é declarado   >>> Gabriela#Chaplin
print("teste", end=" ")
print("... e a continuação")