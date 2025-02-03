import turtle
from turtle import *


'''# Inicializar uma Turtle 
t = Turtle()

# Definir a velocidade
t.speed(1)

# Movimentar a turtle para frente
t.forward(100)

# Movimentar em X graus para a direita
t.right(90)
t.forward(100)

# Movimentar em X graus para a esquerda
t.left(90)
t.forward(100)

# Movimentar a turte para trás
t.backward(200)

input()'''

# Movimento para cima
def cima():
    t.setheading(90)
    t.forward(30)

# Movimento para baixo
def baixo():
    t.setheading(270)
    t.forward(30)

# Movimento para a esquerda
def esquerda():
    t.setheading(180)
    t.forward(30)

# Movimento para a direita
def direita():
    t.setheading(0)
    t.forward(30)


# Criação da turtle
setup(500, 500)
Screen()
t = turtle.Turtle()

# Velocidade da turtle
t.speed(0)
print("Use as setas do teclado para movimentar a Turtle")

listen()
onkey(cima,'Up')
onkey(baixo,'Down')
onkey(esquerda,'Left')
onkey(direita,'Right')

mainloop()
