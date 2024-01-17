class Pessoa:

    def __init__(self, id, nome='Bruno'):
        self.__nome = nome
        self.id = id

    def _set_nome(self, novo_nome):
        self.__nome = novo_nome

    def _get_nome(self):
        return self.__nome

    nome = property(
        fget=_get_nome,
        fset=_set_nome
    )


pessoa = Pessoa(2)
pessoa.nome = 'Carlos'
print(pessoa.nome)