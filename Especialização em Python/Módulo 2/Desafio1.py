from datetime import datetime,timezone
import random

# PROJETO 1 

## Objetivo de projeto

# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1
'''

1. Obtenha o nome do usuário

2. Obtenha a idade do usuário

3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
'''

cartoes = ['R$50,00','R$250,00','R$120,00']

'''
5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
'''

nome_usuario = str(input("Digite seu nome:"))
idade_usuario = int(input("Digite sua idade:"))
data_registro = datetime.now()
print("Data de registro:",format(data_registro,"%d/%m/%Y"))
cartao_usuario = print("Cartão selecionado:",random.choice(cartoes))
aniversario_usuario = datetime.strptime(input('Digite a sua data de nascimento no formato (dd/mm/yyyy):'),'%d/%m/%Y')
print(f"Data de nascimento:{format(aniversario_usuario,'%d/%m/%Y')}")