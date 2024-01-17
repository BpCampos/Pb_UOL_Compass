class Calculo:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def soma(self):
        print(f'Somando: {self.x} + {self.y} = {self.x + self.y}')

    def subtrai(self):
        print(f'Subtraindo: {self.x} - {self.y} = {self.x - self.y}')


conta = Calculo(4, 5)

conta.soma()
conta.subtrai()