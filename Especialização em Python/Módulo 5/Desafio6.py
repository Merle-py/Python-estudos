# Imprimir o e-mail do usuário com id 2
# imprimir a city do usuário com id 1
# Imprimir o total do pedido do usuário com id 2
import json

with open(r'C:\Users\gbern\OneDrive\Área de Trabalho\teste git\projeto-teste\Especialização em Python\Módulo 5\jsonUsuarios\desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["user"][1]["email"])   # Imprimir o e-mail do usuário com id 2
    print(data["user"][0]["address"]["city"])   # imprimir a city do usuário com id 1
    print(data["user"][1]["orders"][0]["total"])   # Imprimir o total do pedido do usuário com id 2