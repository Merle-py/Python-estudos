import json
import os

computador_json = """{
    "marca": "Dell",
    "preço": 15000,
    "id": 1
}"""

# Lendo um string JSON
data = json.loads(computador_json)
print(data["id"])

caminho_arquivo = os.path.join(r'C:\Users\gbern\OneDrive\Área de Trabalho\teste git\projeto-teste\Especialização em Python\Módulo 5','computador.json')

# Salvar um string JSON -> Arquivo JSON
with open(caminho_arquivo,'w',encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)

# Lendo arquio JSON

with open(caminho_arquivo,encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json) # convertendo JSON -> String
    dicionario_computador_json = json.loads(string_computador_json) # Convertendo de String -> Dicionário
    print(dicionario_computador_json["marca"])