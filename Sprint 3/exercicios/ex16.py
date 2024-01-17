def soma_valores(valores):
    inicio = 0
    for i in valores.split(','):
        inicio += int(i)
    print(inicio)


soma_valores("1,3,4,6,10,76")