# A função map serve para passar uma função encima de todos os itens de uma lista

# ​DESAFIO 

# ExtraiA as cores da lista a seguir e coloque as em uma nova lista. Finalmente imprima a nova lista na tela.

pinturas = [

    ['Pintura Classica', 'Azul', 1857],

    ['Pintura Medieval', 'Vermelha', 1867],

    ['Pintura Moderna', 'Verde', 1897]

]

# Primeira forma
cores1 = []
for pintura in pinturas:
    cores1.append(pintura[1])
print(cores1)

# Segunda forma
def extrair_cor(cor):
    return cor[1]
cores2 = list(map(extrair_cor,pinturas))
print(cores2)