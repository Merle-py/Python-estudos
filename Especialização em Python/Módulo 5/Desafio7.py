import json
import os

desafio_json = """{
    "name":"Jhon",
    "age":30,
    "city":"New York",
    "isStudent":true,
    "gpa":3.5
}"""

caminho_arquivo = os.path.join(r'C:\Users\gbern\OneDrive\Área de Trabalho\teste git\projeto-teste\Especialização em Python\Módulo 5','desafio.json')

with open(caminho_arquivo,'w',encoding='utf-8') as arquivo_json:
    json.dump(desafio_json,arquivo_json)