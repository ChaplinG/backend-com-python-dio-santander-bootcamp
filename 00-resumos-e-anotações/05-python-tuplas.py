# Armazenam de maneira sequencial qualquer tipo de objeto; mas são IMUTÁVEIS
# objetos podem ser acessados através de índices também, contando a partir de 0


frutas = ("laranja", "pera", "uva",)
#como o parênteses é utilizado pra precedência de operações, coloca-se vírgula antes de fechar os parênteses no caso da tupla
print(frutas[0])
print(frutas[-1])

letras = tuple("python")
#"tuple" já tá sendo puxado, não precisa da vírgula

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)


#---TUPLAS ANINHADAS
# pode-se armazenar tuplas dentro de outras tuplas
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)
#   matriz[índice][coluna]
print(matriz[0])        #pega todo o primeiro índice "[1, 'a', 2]"
print(matriz[0][0])     #pega o objeto do primeiro índice, na primeira coluna "1"
print(matriz[1][2])     #pega o objeto do 2º índice, na 3ª coluna "4"
print(matriz[-1][2])    #pega o objeto no último índice, na 3ª coluna "c"


#---FATIAMENTO
# além do acesso direto, também é possível extrair um cjto de valores de uma sequência
# se passa o índice inicial e/ou final para acessar o conjunto
# é possível informar quantas posições o cursor deve pular no acesso
curso = ("p", "y", "t", "h", "o", "n")

#   [início : fim : "pulo"]
print(curso[:2])        # ['p', 'y']
print(curso[2:])        # ['t', 'h', 'o', 'n']
print(curso[1:3])       # ['y', 't']
print(curso[0:6:2])     # ['p', 't', 'o']
print(curso[::])        # ['p', 'y', 't', 'h', 'o', 'n']
print(curso[::-1])      # ['n', 'o', 'h', 't', 'y', 'p']


#---ITERAR TUPLA
# ver todos os valores dentro da lista
carros = ("gol", "celta", "palio", "picape", "jipe",)

for carro in carros:
    print(carro)


#---[].index
# retorna em qual índice está a primeira ocorrência do objeto procurado
print(carros.index("jipe"))     # 4
print(carros.index("gol"))      # 0


#---len
print(len(carros))

carros2 = ("gol")
print(isinstance(carros2, tuple))