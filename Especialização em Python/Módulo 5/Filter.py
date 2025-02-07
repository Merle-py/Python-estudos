# A diferença entre o filter e o map processa e retorna todos os valores, já o
# filter trabalha com true e false

nomes = ['marcos','Larissa','Gabriel','Iris']

def pessoa_aprovada(pessoa):
    if pessoa == 'marcos':
        return True
    return False

print(list(filter(pessoa_aprovada,nomes)))
print(list(map(pessoa_aprovada,nomes)))


pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

def pintura_antiga(pintura):
    if pintura[2] <= 1870:
        return True
    return False

print(list(filter(pintura_antiga,pinturas)))
