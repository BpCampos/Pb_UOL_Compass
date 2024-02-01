def maiores_que_media(conteudo: dict) -> list:
    valores = [(x, y) for x, y in conteudo.items()]

    soma = 0

    for preco in valores:
        soma += preco[1]

    media = soma / len(valores)

    resultado = filter(lambda r: r[1] > media, valores)

    print(sorted(list(resultado), key=lambda x: x[1]))
