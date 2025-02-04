'''
def depositando_dinhero():
    print('depositando dinheiro')

    def depositando_reais():
        print('depositando reais')
    
    def depositando_dolares():
        print('depositando dolares')

    depositando_reais()
    depositando_dolares()

depositando_dinhero()

def pai(numero):
    def filho_1():
        print('Filho 1')
    def filho_2():
        print('Filho 2')
    if numero == 1:
        return filho_1
    
resultado = pai(1)
resultado()
'''
def meu_decorator(funcao):
    def wrapper():
        print('antes')
        funcao()
        print('depois')
    return wrapper

def funcao():
    print('teste')

resultado = meu_decorator(funcao)
resultado()

# Existe uma outra forma de fazer isso mais facilmente:

def meu_decorator(funcao):
    def wrapper():
        print('antes')
        funcao()
        print('depois')
    return wrapper

@meu_decorator
def teste():
    print('teste')

teste()

# Chamando teste, ele será usado como argumento da função meu_decorator