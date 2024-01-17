with open('actors.csv', 'r') as actors:
    content = actors.readlines()

value_only = content[1:]

total_gross = []

for i in value_only:
    if i.split(',')[1] == ' Jr."':
        total_gross.append(
            i.split(',')[2] + ', ' + i.split(',')[0] + i.split(',')[1])
    else:
        total_gross.append(i.split(',')[1] + ', ' + i.split(',')[0])

with open('etapa-5.txt', 'w', encoding='utf-8') as etapa5:
    for content in total_gross:
        etapa5.write(f'{content.split(',')[1]} -  {content.split(',')[0]}\n')
