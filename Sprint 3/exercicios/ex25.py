class Avião:

    cor = 'azul'

    def __init__(self, modelo, velocidade_maxima, capacidade) -> None:
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade


aviao1 = Avião('BOIENG456', 1500, 400)
aviao2 = Avião('Embraer Praetor 600', 863, 400)
aviao3 = Avião('Antonov An-2', 258, 12)


avioes = [aviao1, aviao2, aviao3]

for i in avioes:
    print(f'O avião de modelo {i.modelo} possui uma velocidade máxima de {
          i.velocidade_maxima} capacidade para {i.capacidade} passageiros e é da cor {i.cor}')