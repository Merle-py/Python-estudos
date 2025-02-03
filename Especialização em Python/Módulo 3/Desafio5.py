# Imprima na tela a marca + celular de todos os celulares, usando as informações abaixo

celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']

versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'Marca: {celular} --- Versao: {versao}')