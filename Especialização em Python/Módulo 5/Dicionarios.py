# Dicionários

# Nome
# Idade
# Altura

# Dicionário(chave,valor)
dicionario_pessoa = {'nome': 'Gabriel','idade': 24, 'altura': 1.77}
print(dicionario_pessoa)

dicionario_pessoa2 = dict(nome='Gabriel',idade=24,altura=1.77)
print(dicionario_pessoa2)
print(dicionario_pessoa2['idade'])

# Maneira mais fácil para descobrir quais chaves e valores estão no dicioáario
print(dicionario_pessoa2.keys())
print(dicionario_pessoa2.values())
print(dicionario_pessoa2.items())

# Iterando sobre um dicionário
for item in dicionario_pessoa2.items():
    print(item)
    print(item[1])