def conta_vogais(texto: str) -> int:
    vogais = filter(lambda v: v.upper() == 'A' or v.upper() == 'E' or v.upper() ==
                    'I' or v.upper() == 'O' or v.upper() == 'U', texto)

    return len(list(vogais))
