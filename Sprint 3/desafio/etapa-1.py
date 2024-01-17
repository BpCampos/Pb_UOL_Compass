movie_numbers = []
actor = []

with open('actors.csv') as actors:
    for content in actors:
        if len(content.split(',')) > 7:
            movie_numbers.append(content.split(',')[3])
            actor.append(content.split(',')[0] + content.split(',')[1])
        elif content.split(',')[2] == 'Number of Movies':
            continue
        else:
            movie_numbers.append(content.split(',')[2])
            actor.append(content.split(',')[0])


with open('etapa-1.txt', 'w', encoding='utf-8') as etapa1:
    etapa1.write(f'O ator/atriz com o maior número de filmes é {actor[movie_numbers.index(
        max(movie_numbers))]} com {movie_numbers[movie_numbers.index(max(movie_numbers))]} filmes')
