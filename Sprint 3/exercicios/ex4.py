def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


for i in range(1, 101):
    if eh_primo(i) == True:
        print(i)