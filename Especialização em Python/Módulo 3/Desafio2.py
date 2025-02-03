# Desafio 

# Monte o seguinte cenário usando condicionais

# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras

# Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices

# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário

cabelo = 40

# Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
if(cabelo <= 20):
    print("Valor a pagar: R$50,00")

# Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
elif 21 <= cabelo <= 30:
    print("Valor a pagar: R$70,00")

# Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
elif 31 <= cabelo <= 50:
    print("Valor a pagar: R$100,00")

# Acima de 50cm Favor consultar na recepção '''
elif cabelo > 50:
    print("Favor consultar valor na recepção")
