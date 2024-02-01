from functools import reduce


def calcula_saldo(lancamentos) -> float:
    valores = map(lambda v: v[0] * -1 if v[1] == 'D' else v[0], lancamentos)
    saldo = reduce(lambda x, y: x + y, valores)
    return saldo
