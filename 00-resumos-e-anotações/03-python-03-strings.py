#MÉTODOS ÚTEIS DA CLASSE STRING
curso = "    cuRso De pYtHon  "

print(curso.upper())            #    CURSO DE PYTHON  
print(curso.lower())            #    curso de python
print(curso.title())            #    Curso De Python

print(curso.strip())            #"cuRso De pYtHon"
print(curso.lstrip())           #"cuRso De pYtHon  "
print(curso.rstrip())           #"   cuRso De pYtHon"

print(curso.center(25, "#"))    #add caracteres, definidos no 1º parâmetro, até que o número de char fique igual ao 2º parâmetro

print(".".join(curso))          # . . . .c.u.R.s.o. .D.e. .p.Y.t.H.o.n. .


##INTERPOLAÇÃO DE VARIÁVEIS -> 3 formas
nome = "Gabriela"
idade = 26
profissao = "Ilustradora"
linguagem = "Python"
PI = 3.14159

# 1ª usando o sinal %, a MENOS recomendada; old style
print("Olá! Me chamo %s. Tenho %d anos de idade, atualmente trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

# 2ª método format, evolução do old style
print("Olá! Me chamo {}. Tenho {} anos de idade, atualmente trabalho como {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))
print("Olá! Me chamo {3}. Tenho {2} anos de idade, atualmente trabalho como {1} e estou matriculado no curso de {0}".format(linguagem, profissao, idade, nome))
pessoa = {"nome": nome, "idade": idade, "profissao": profissao, "linguagem": linguagem}
print("Olá! Me chamo {nome}. Tenho {idade} anos de idade, atualmente trabalho como {profissao} e estou matriculado no curso de {linguagem}".format(**pessoa)) #utiliza dicionário

# 3ª utilizando f strings, a mais recomendada
print(f"Olá! Me chamo {nome}. Tenho {idade} anos de idade, atualmente trabalho como {profissao} e estou matriculado no curso de {linguagem}")
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")


#FATIAMENTO DE STRING
#técnica utilizada p/ retornar substrings (partes da string original)
#informa início (start), fim (stop) e passo (step)      [start: stop[, step]]
nome = "Gabriela Chaplin"

print(nome[0])      #"G"
print(nome[:])      #segue normal
print(nome[:9])     #"Gabriela" sem parâmetro no start, starta no 0, termina no 9º caractere
print(nome[9:])     #"Chaplin" sem parâmetro no stop, vai até o final, iniciando no 9º caractere
print(nome[3:11])   #"riela Ch"
print(nome[0:21:3]) #"GrlCpn"
print(nome[-1])     #usando negativo, corre na string do fim ao começo, iniciando no 1
print(nome[::-1])   #nilpahC aleirbaG


#STRINGS MÚLTIPLAS/TRIPLAS
mensagem = f"""
Olá, meu nome é {nome}.
Estou aprendendo Python.
    E a mensagem mantém os recuos."""
print(mensagem)

print("""
    ========= MENU =========
      
      1 - Extrato
      2 - Saque
      3 - Depósito

    ========================
      """)