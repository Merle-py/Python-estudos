import json

with open(r'C:\Users\gbern\OneDrive\Área de Trabalho\teste git\projeto-teste\Especialização em Python\Módulo 5\jsonUsuarios\usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter um arquivo json para uma string
    print(data["nome"])

with open(r'C:\Users\gbern\OneDrive\Área de Trabalho\teste git\projeto-teste\Especialização em Python\Módulo 5\jsonUsuarios\usuarios2.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) 
    print(data["permissões"][1])

with open(r'C:\Users\gbern\OneDrive\Área de Trabalho\teste git\projeto-teste\Especialização em Python\Módulo 5\jsonUsuarios\usuarios3.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) 
    print(data["usuários"][0]["permissões"][1])
    print(data["usuários"][1]["admin"])
    print(data["usuários"][0]["telefone"])