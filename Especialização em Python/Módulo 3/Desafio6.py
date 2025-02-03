# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
valor = 1
while valor <= 120:
    print(valor)
    valor += 1

# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
senha = input("Digite sua senha:")
while senha != 'secreto':
    print("Senha incorreta!")
    senha = input("Digite sua senha:")

# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1
valor = 100
while valor >= 1:
    print(valor)
    valor -= 1