valores = list(range(1,10))
anos = list(range(2020,2061,20))
print(valores+anos)

# Adiciona valores ao final da lista
valores.append(10)

# Unir listas
valores.extend(anos)
print(valores)

# Adicionar lista
nova_lista = valores+anos
print(nova_lista)

# Inserir
anos.insert(2,'teste')
print(anos)

# Extrair com base no indice - também remove da lista original
anos_2020 = anos.pop(0)
print(anos_2020)
print(anos)

# Remover item da lista
anos.remove('teste')
print(anos)
# A função del pode receber tanto um índice inicial como um índice final
# para fazer a remoção de uma faixa de valores
del valores[1:5]
print(valores)

# Contando as ocorrências de um valor
print(valores.count(1))

# Resetar lista
valores.clear()
print(valores)