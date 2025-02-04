'''
Desafio

Crie um decorador que irá pegar a função que for passado
para ele e imprimir o horário atual antes de executar a
função e depois imprima o horário após ter finalizado a
execução da função

'''

from datetime import datetime
from time import sleep

def funcao(decorador):
    print(datetime.now())
    sleep(1)
    decorador()

@funcao
def decorador():
    print(datetime.now())