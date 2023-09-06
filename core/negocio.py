import abc
import random


# TODO: Implementar jogos para lotofacil e lotomania

class Jogo(abc.ABC):

    @abc.abstractmethod
    def sortear(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class Megasena(Jogo):

    def __init__(self):
        self.numeros = [i for i in range(1, 61)]
        self.sorteados = []

    def sortear(self, quantidade=6):
        if quantidade >= 6:
            self.quantidade = quantidade
        else:
            self.quantidade = 6

        self.sorteados = sorted(random.sample(self.numeros, k=self.quantidade))

    def __len__(self):
        return len(self.sorteados)

    def __getitem__(self, item):
        return self.sorteados[item]

    def __str__(self):
        return str(self.sorteados)


class Quina(Jogo):

    def __init__(self, ):
        self.numeros = [i for i in range(1, 81)]
        self.sorteados = []

    def sortear(self, quantidade=5):
        if quantidade >= 5:
            self.quantidade = quantidade
        else:
            self.quantidade = 5

        self.sorteados = sorted(random.sample(self.numeros, k=self.quantidade))

    def __len__(self):
        return len(self.sorteados)

    def __getitem__(self, item):
        return self.sorteados[item]

    def __str__(self):
        return str(self.sorteados)
