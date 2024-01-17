primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

nomes = enumerate(primeirosNomes)

n = 0

for i, j in nomes:
    print(f'{i} - {j} {sobreNomes[n]} está com {idades[n]} anos')
    n += 1