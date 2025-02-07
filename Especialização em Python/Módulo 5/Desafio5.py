# DESAFIO 1 🥇

'''

Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500

'''

vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]    

def salario_acima(salario):
    if salario[1] > 2500:
        return True
    return False

print(list(filter(salario_acima,vagas)))