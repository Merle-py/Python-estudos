## Módulo 2 - Gerar apresentação do usuário

### Funcionalidades do módulo 2 - Mensagem de boas vindas!
'''
Usando os dados obtidos no módulo 1, exiba as seguintes informações:

1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).

Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''

cartoes = ['R$50,00','R$250,00','R$120,00']

nome_usuario = str(input("Digite seu nome:"))
idade_usuario = int(input("Digite sua idade:"))
data_registro = datetime.now()
print("Data de registro:",format(data_registro,"%d/%m/%Y"))
aniversario_usuario = datetime.strptime(input('Digite a sua data de nascimento no formato (dd/mm/yyyy):'),'%d/%m/%Y')
cartao_usuario = print("Parabéns! Houve um sorteio e você ganhou um vale-compras no valor de ",random.choice(cartoes))
print(f"Data de nascimento:{format(aniversario_usuario,'%d/%m/%Y')}")