with open('actors.csv', 'r') as actors:
    content = actors.readlines()

    value_only = content[1:]

    gross = [value.split(',')[-1] for value in value_only]

    average_gross = sum(float(value) for value in gross) / len(gross)

    total_gross = sum(float(value) for value in gross)

    print(total_gross / 50)

with open('etapa-2.txt', 'w', encoding='utf-8') as etapa2:
    etapa2.write(f'Apresente a média de receita de bilheteria bruta dos principais filmes é {
                 average_gross}')
