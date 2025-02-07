# Set aceita adicionar novos valores, porém não aceita valores repetidos

numeros = [1,2,2,3,5]
frutas = {'banana','maca','goiaba','banana'}

set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

set_numeros.add(10)
print(set_numeros)
set_numeros.add(10) # Não repetiu
print(set_numeros)

# Conjuntos 
numeros1 = [1,2,2,5,6]
numeros2 = [2,3,5,8,9]

a = set(numeros1)
b = set(numeros2)

print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))