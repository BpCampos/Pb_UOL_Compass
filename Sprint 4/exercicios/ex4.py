def calcular_valor_maximo(operadores, operandos) -> float:
    x = zip(operandos, tuple(operadores))

    resultado = list(
        map(lambda r: eval(str(r[0][0]) + r[1] + str(r[0][1])), x))

    return max(resultado)
