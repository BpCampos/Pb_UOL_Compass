import random

numeros = []

for i in range(250):
    numeros.append(random.randint(0, 500))

print(list(reversed(numeros)))
