# Trabalhando com multiplas listas usando ZIP
from itertools import zip_longest

a_lista = ['a','b','c','d','e']
b_lista = [1, 2, 3, 4, 5]

for a,b in zip(a_lista,b_lista):
    print(a)
    print(b)
    
c_lista = ['a','b','c','d','e','f']
d_lista = [1, 2, 3, 4, 5]

# Para trabalhar com multiplas listas de tamanhos diferente, se usa o zip_longest
for c,d in zip_longest(c_lista,d_lista):
    print(f'{c} {d}')
    