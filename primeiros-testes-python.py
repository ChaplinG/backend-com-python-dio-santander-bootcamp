print("Hello world!")

# Modo interativo
# dir()   e   help()

age, name = (26, 'Gabriela')    #VARIÁVEIS
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

name = input("Informe seu nome: ")
print(f'Meu nome é {name}')

RG = 1230032145 #CONSTANTE, nome da variável todo em maiúsculo

ABS_PATH = '/home/chaplin/Bootcamp Santander Backend com Python'    #constante
BRAZILIAN_STATES = ['SP', 'RJ', 'MG', 'SC', 'RS',]
print(BRAZILIAN_STATES)

numero_inteiro = 10
preco_quebrado = float(numero_inteiro) #pra converter tipo, pode-se usar o comando, como int() ou string() etc
print(preco_quebrado)
preco_quebrado = numero_inteiro/4      #dependendo da operação, ela vai converter automaticamente
print(preco_quebrado)

print(numero_inteiro/2)    #a divisão converte pra float, mesmo que o resultado não fique quebrado
print(numero_inteiro//2)   #com barra dupla o resultado vai pra inteiro, caso o resultado seja quebrado, ele arredonda
print(numero_inteiro//4)

str(numero_inteiro)

numero_escrito = f'o resultado é {numero_inteiro}'
print(numero_escrito)

#a conversão nem sempre é possível:
preco = 'python'
print(preco)
#print(float(preco))

valor = '20'
print(float(valor))

#builtins input() e print()
nome = "Gabriela"
sobrenome = "Chaplin"

print(nome, sobrenome)              #por padrão, o separador é um espaço em branco              >>> Gabriela Chaplin
print(nome, sobrenome, end="...\n") #add reticências no final e /n insere uma troca de linha    >>> Gabriela Chaplin...
print(nome, sobrenome, sep="#")     #insere o sep em todos os espaços entre o que é declarado   >>> Gabriela#Chaplin
print("teste", end=" ")
print("... e a continuação")