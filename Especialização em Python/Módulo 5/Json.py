import json

with open('arquivos_json_usuarios/usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter um arquivo json para uma string
    print('')