with open('actors.csv', 'r') as actors:
    content = actors.readlines()

    value_only = content[1:]

    average_movie = [float(value.split(',')[-3]) for value in value_only]

    highest_average = max(average_movie)

    actor_answer = [value.split(
        ',')[0] for value in value_only][average_movie.index(highest_average)]

    with open('etapa-3.txt', 'w', encoding='utf-8') as etapa3:
        etapa3.write(
            f'o ator/atriz com a maior média de receita de bilheteria bruta por filme é {actor_answer}')
