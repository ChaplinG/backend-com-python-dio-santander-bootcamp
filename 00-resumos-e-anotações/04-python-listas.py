# Armazenam de maneira sequencial qualquer tipo de objeto; são MUTÁVEIS
# pode-se utilizar o list, a função range ou colocando valores separados por vírgula dentro de []
# é aplicado o conceito de PILHA

frutas = []         #pode declarar ela vazia
frutas = ["laranja", "maçã", "uva"]
print(frutas[2])    #valores podem ser acessados através de índices, começando no 0
print(frutas[-3])   #de trás pra frente com o sinal negativo, começando no -1

letras = list("python")
print(letras)       #['p', 'y', 't', 'h', 'o', 'n']

numeros = list(range(10))
print(numeros)      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]


#---ITERAR LISTA
# ver todos os valores dentro da lista
carros = ["gol", "celta", "palio", "picape"]

print("ITERAR LISTA")
for carro in carros:
    print(carro)


#---[].append
# add itens, por padrão no final da fila
carros.append("jipe")
carros2 = carros.copy()


#---FUNÇÃO ENUMERATE
# para saber qual o índice do objeto dentro do laço for
print("ENUMERATE")
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


#---[].index
# retorna em qual índice está a primeira ocorrência do objeto procurado
print(carros.index("jipe"))     # 4
print(carros.index("gol"))      # 0


#---[].clear
# limpa a lista
carros.clear()
print(carros)


#---[].copy
# salva cópia de uma lista numa nova instância
lista1 = [1, "Python", [40, 30, 20]]
lista2 = lista1.copy()
print(id(lista1), id(lista2))

print(carros2)


#---[].count
# conta quantas vezes o objeto indicado aparece dentro da lista
cores = ["vermelho", "roxo", "amarelo", "roxo", "rosa", "amarelo", "roxo"]

print(cores.count("vermelho"))  # 1
print(cores.count("roxo"))      # 3
print(cores.count("amarelo"))   # 2


#---[].extend
# add mais de um objeto, até mesmo uma lista inteira
carros2.extend(cores)
print(carros2)


#---[].pop
# a cada pop vai trazendo o próximo objeto no topo da PILHA, caso não seja indicado o índice
# remove os objetos da pilha, através do índice
print(carros2.pop())
print(carros2.pop())
print(carros2.pop())
print(carros2.pop(0))
print(f"Carros2 após .pop(): {carros2}")


#---[].remove
# remove através do objeto, e não do índice
print("REMOVE")
carros2.remove("roxo")
print(carros2)


#---[].reverse
# espelha a lista
carros2.reverse()
print(carros2)


#---len
print(len(carros2))


#---LISTA ANINHADA
# uma lista pode armazenar outras listas, criando estruturas bidimensionais (tabelas, com índices e também colunas)
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
#   matriz[índice][coluna]
print(matriz[0])        #pega todo o primeiro índice "[1, 'a', 2]"
print(matriz[0][0])     #pega o objeto do primeiro índice, na primeira coluna "1"
print(matriz[1][2])     #pega o objeto do 2º índice, na 3ª coluna "4"
print(matriz[-1][2])    #pega o objeto no último índice, na 3ª coluna "c"


#---FATIAMENTO
# além do acesso direto, também é possível extrair um cjto de valores de uma sequência
# se passa o índice inicial e/ou final para acessar o conjunto
# é possível informar quantas posições o cursor deve pular no acesso
curso = ["p", "y", "t", "h", "o", "n"]

#   [início : fim : "pulo"]
print(curso[:2])        # ['p', 'y']
print(curso[2:])        # ['t', 'h', 'o', 'n']
print(curso[1:3])       # ['y', 't']
print(curso[0:6:2])     # ['p', 't', 'o']
print(curso[::])        # ['p', 'y', 't', 'h', 'o', 'n']
print(curso[::-1])      # ['n', 'o', 'h', 't', 'y', 'p']


#---COMPREENSÃO DE LISTA
# tem uma sintaxe mais curta quando se deseja criar uma nova lista com base nos valores de uma lista existente (fitro)
# ou gerar uma nova lista modificando os elementos de uma lista existente
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
#   OU
pares = [numero for numero in numeros if numero % 2 == 0]
# o primeiro "numero" é o retorno, o que vem do for em diante é similar ao for na linha 68
print(pares)
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)
#   OU
quadrado = [(numero ** 2) for numero in numeros]
print(quadrado)


#---[].sort
linguagens = ["python", "js", "c#", "java", "kotlin"]
linguagens.sort()               #ordena alfabeticamente
print(linguagens)

linguagens.sort(reverse= True)  #ordena o inverso de alfabeticamente
print(linguagens)

linguagens.sort(key= lambda x: len(x))                  #ordena por quantidade de caractere
print(linguagens)

linguagens.sort(key= lambda x: len(x), reverse= True)   #ordena o inverso do tamanho da palavra
print(linguagens)

print(sorted(linguagens, key= lambda x: len(x)))        #o mesmo que .sort(), mas colocada como função