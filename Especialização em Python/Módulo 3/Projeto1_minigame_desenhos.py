from turtle import Turtle
import keyboard

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


# Criação da turtle
t = Turtle()

# Velocidade da turtle
t.speed(1)
print("Use as setas do teclado para movimentar a Turtle\nPressione 1 para sair")

while not keyboard.press("1"):
    # Movimento para cima

    if keyboard.press("up"):
        t.setheading(90)
        t.forward(1)
        while keyboard.is_pressed("up"):
            pass
    # Movimento para baixo
    elif keyboard.press("down"):
        t.setheading(270)
        t.forward(1)
        while keyboard.is_pressed("down"):
            pass
    
    # Movimento para a esquerda
    elif keyboard.press("left"):
        t.setheading(180)
        t.forward(1)
        while keyboard.is_pressed("left"):
            pass
    
    # Movimento para a direita
    elif keyboard.press("right"):
        t.setheading(0)
        t.forward(1)
        while keyboard.is_pressed("right"):
            pass