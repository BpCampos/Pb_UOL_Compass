import random

random_list = random.sample(range(500), 50)

sorted_list = sorted(random_list)

lista_mediana = sorted_list[len(random_list) //
                            2 - 1: len(random_list) // 2 + 1]
mediana = 0

for i in lista_mediana:
    mediana += i
mediana /= 2

media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print('Media: {}, Mediana: {}, Mínimo: {}, Máximo: {}'.format(
    media, mediana, valor_minimo, valor_maximo))