lista = set(('abc', 'abc', 'abc', '123', 'abc', '123', '123'))

nova_lista = []

for i in lista:
    if i not in nova_lista:
        nova_lista.append(i)

print(nova_lista)