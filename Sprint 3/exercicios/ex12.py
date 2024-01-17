import json

arquivo = open('person.json')
dados = arquivo.read()
arquivo.close()

dados_brutos = json.loads(dados)

print(dados_brutos)