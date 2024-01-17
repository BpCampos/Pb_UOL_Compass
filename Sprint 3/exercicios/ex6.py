a = {1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
comum = []


def compara(set_a, set_b):
    for i in set_a:
        for j in set_b:
            if i == j:
                comum.append(j)
    print(comum)


compara(a, b)