#CONJUNTO NÃO ORDENADO DE PARES chave:valor
# as chaves são únicas, IMUTÁVEIS; os objetos que acompanham podem ser quaisquer um
# delimitado por {}, lista de chave:valor separados por vírgula
# funciona como PILHA


pessoa = {"nome": "Guilherme", "idade": 28}     # pode ser declarado com {}

pessoa = dict(nome="Guilherme", idade = 28)     # ou usando o dict()


#---ADD NOVO PAR chave:valor
pessoa["telefone"] = "3311-2799"
print(pessoa)
print(pessoa["nome"])


#---ALTERAR VALORES
pessoa["nome"] = "Gabriela"
pessoa["idade"] = 26
print(pessoa)


#---DICIONÁRIOS ANINHADOS
# dicionário pode armazenar outro dicionário nele

# "chave": {dicionário interno}
contatos = {
    "chaplin@gmail.com": {"nome": "Gabriela", "idade": 27},
    "estella@gmail.com": {"nome": "Estella", "idade": 26},
    "palloma@gmail.com": {"nome": "Palloma", "idade": 25},
}

print(contatos["chaplin@gmail.com"]["idade"])


#---ITERAÇÃO
for chave in contatos:
    print(chave, contatos[chave])       #não é a mais recomendada

for chave, valor in contatos.items():   #items() retorna uma lista de tuplas, onde 1º argumento é chave, 2º é valor
    print(chave, valor)


#---{}.items
print(f"ITEMS: {contatos.items()}")


#---{}.copy
# copia o dicionário
contatos2 = contatos
print(contatos2)


#---{}.get
# caso chame uma chave inexistente pelo método simples contato["chave"], o programa dá erro e encerra a execução
# pra evitar isso, pode-se utilizar o {}.get
contatos2.get("chave")          # retorna none se inexistente
contatos2.get("chave", {})      # retorna {}
print(f"GET: {contatos2.get("chaplin@gmail.com")}")
print(f"GET: {contatos2.get("chaplin@gmail.com", {})}")


#---{}.clear
# apaga tudo
#contatos.clear()


#---{}.keys
# retorna só as chaves do dicionário
print(f"KEYS: {contatos2.keys()}")


#---{}.values
# diferente do keys, retorna todos os valores do dicionário
print(f"VALUES: {contatos2.values()}")


#---{}.pop
# remove do dicionário
# se encontrar o parâmetro passado remove, se não encontrar correspondente retorna o parâmetro passado ("não encontrado" nesse caso)
contatos2.pop("estella@gmail.com", "não encontrado")
print(contatos2)


#---{}.popitem
# quando não se informa qual item quer remover, popitem remove na sequência, usando lógica da PILHA
print(f"Antes do PopItem: {contatos2}")
contatos2.popitem()
print(f"PopItem: {contatos2}")


#---{}.fromkeys
# cria chaves mesmo que ainda não haja valor pra elas (deixa como none)

dicionario1 = dict.fromkeys(["nome", "telefone"])
# cria o dicionário atribuindo "none" como valor pradrão pras chaves passadas como parâmetro

dicionario2 = dict.fromkeys(["nome", "idade"], "vazio")
# cria o dicionário declarando parâmetro passado ("vazio") como padrão pras chaves que não tiverem valor atribuído

print(f"dicionário com none: {dicionario1}")
print(f"dicionário com vazio: {dicionario2}")


#---{}.setdefault
professor = {"nome": "Guilherme", "telefone": "3333-2221"}

# se a chave já existir, ele não altera nada
professor.setdefault("nome", "Giovana")

# se a chave ainda não existir, ele cria e atribui o valor passado
professor.setdefault("idade", 28)


#---{}.update
# diferente do setdefault, altera o valor
professor.update({"nome": "Giovana"})
print(professor)


#--- in
# verifica se a chave está no dicionário ou não
print("gabi.chaplin@gmail.com" in contatos2)    #False
print("chaplin@gmail.com" in contatos2)         #True


#--- del
professores = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 28},
    "palloma@gmail.com": {"nome": "Palloma", "idade": 25},
    "estella@gmail.com": {"nome": "Estella", "idade": 26},
    "chaplin@gmail.com": {"nome": "Gabriela", "idade": 26},
}

del professores["estella@gmail.com"]["idade"]   #apaga somente a idade do objeto
del professores["palloma@gmail.com"]            #apaga todo o objeto
print(professores)