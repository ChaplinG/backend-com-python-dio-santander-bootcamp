#CONJUNTOS ou SETS
# uma coleção sem objetos repetidos, utilizado para representar cjtos matemáticos ou eliminar itens duplicados de um iterável
# pode ser declarado utilizando [] ou {}
# funciona como FILA, e não pilha


#---SET
# passa uma lista pro set e ele elimina os objetos duplicados
numeros = [1 ,2, 3, 1, 4, 5]
print(set(numeros))

numeros2 = list(numeros)
numeros2[0]
# para os objetos serem acessados por índices, é necessário transformar o set em uma lista


#---{}.union
cjto_a = {1, 2, 3}
cjto_b = {4, 6}
cjto_c = {1, 2, 3, 5}

print(cjto_a.union(cjto_b))


#---{}.intersection
print(cjto_a.intersection(cjto_b))


#---{}.difference
print(cjto_a.difference(cjto_b))
print(cjto_b.difference(cjto_a))


#---{}.symmetric_difference
print(cjto_a.symmetric_difference(cjto_b))


#---{}.issubset
print(cjto_a.issubset(cjto_b))      #False
print(cjto_a.issubset(cjto_c))      #True


#---{}.issuperset
print(cjto_a.issuperset(cjto_c))    #False
print(cjto_c.issuperset(cjto_a))    #True


#---{}.isdisjoint
print(cjto_a.isdisjoint(cjto_b))    #True
print(cjto_a.isdisjoint(cjto_c))    #False


#---{}.add
# pode se passar um elemento e, se ele ainda não existir, vai ser add
sorteio = {1, 2}

sorteio.add(2)
print(sorteio)

sorteio.add(3)
sorteio.add(4)
sorteio.add(5)
print(sorteio)


#---{}.discard
sorteio.discard(1)
print(sorteio)


#---{}.remove
# diferente do discard, se remover um elemento inexistente eele dá erro informando


#---{}.len
print(sorteio)
print(f"LEN: {len(sorteio)}")


#---{}.in
print(1 in sorteio)     #False
print(3 in sorteio)     #True


#---{}.pop
print(sorteio.pop())
print(sorteio)


#---{}.clear
sorteio.clear()
print(sorteio)