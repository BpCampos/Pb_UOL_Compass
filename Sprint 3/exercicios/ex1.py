import datetime

x = datetime.datetime.now()
nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

print((100 - idade) + x.year)
