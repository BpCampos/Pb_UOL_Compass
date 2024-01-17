class Passaro:
    def __init__(self, nome, som) -> None:
        self.nome = nome
        self.som = som

    def voar(self):
        print(self.nome)
        print('voando...')

    def emitir_som(self):
        print(f'{self.nome} emitiando som...')
        print(f'{self.som}')


class Pato(Passaro):
    def __init__(self, nome, som) -> None:
        super().__init__(nome, som)


class Pardal(Passaro):
    def __init__(self, nome, som) -> None:
        super().__init__(nome, som)


pato = Pato('Pato', 'Quack Quack')

pardal = Pardal('Pardal', 'Piu Piu')

pato.voar()
pato.emitir_som()
pardal.voar()
pardal.emitir_som()