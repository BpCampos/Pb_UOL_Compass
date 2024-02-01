import csv

with open('estudantes.csv', 'r') as file:
    content = sorted(csv.reader(file))

    for i in content:
        notas_int = list(map(lambda n: int(n), i[1:]))
        print(f'Nome: {i[0]} Notas: {sorted(notas_int, reverse=True)[:3]} Média: {
              round(sum(sorted(notas_int, reverse=True)[:3]) / 3, 2)}')
