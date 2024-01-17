with open('actors.csv', 'r') as actors:
    content = actors.readlines()

value_only = content[1:]

maior_bilheteria = [value.split(',')[-2] for value in value_only]

vezes_que_apareceu = []

for i in maior_bilheteria:
    contador = 0
    for j in maior_bilheteria:
        if i == j:
            contador += 1
    vezes_que_apareceu.append(str(contador) + ',' + i)

set_filmes = set(vezes_que_apareceu)

with open('etapa-4.txt', 'w', encoding='utf-8') as etapa4:
    index = 1
    for content in sorted(set_filmes, reverse=True):
        etapa4.write(f'{index} O filme {content.split(',')[1]} aparece {
                     content.split(',')[0]} vez(es) no dataset\n')
        index += 1
