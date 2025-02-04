Existem 2 tipos de funções:

1.Argumentos posicionais;
2.Argumentos nomeados.

def aluno(nome,sombrenome)
    pass

aluno(gabriel,bernardo)  ---  argumentos posicionais

aluno(sobrenome=bernardo,nome=gabriel)   ---   argumentos nomeados

Caso eu queira que os argumentos sejam obrigatoriamente nomeados, devo adicionar '*'

def aluno(nome,*,sombrenome)   ---   somente sobrenome será obrigatório ser nomeado
    pass

def aluno(*,nome,sombrenome)   ---   tudo deverá ser nomeado
pass

--------------------------------------------------------------------------------------

*Args - Funções com n° de argumentos dinâmicos

def somar(*valores, b):
    for valor in valores:
        b += valor
    return(b)

Esse asterisco em valores fará com que possam ser colocados quantos
argumentos eu quiser na variável valores, que terá type tupla.
Também é importante lembrar que após valores, b deverá ser nomeado

Ex:
soma(2,3,4,b=5)

--------------------------------------------------------------------------------------

**Kwargs - Funções com n° de argumentos nomeados dinâmicos

def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a = 'Teste', b = 'Teste 2', c = 'palavra')

Exemplo Args e Kwargs:

def funcao(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)   ---   Argumentos nomeados são passados na forma de dicionário 
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

funcao = (gabriel, 1, 2, 3, 4, a = 'aa', b = 'bb', c = 'cc')