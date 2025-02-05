from random import randint

valores = list(randint(2,30) for i in range(1,10))
print(valores)

# Organizar uma lista
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)

# Lista em forma reversa sem ser organizada
valores.reverse()
print(valores)

