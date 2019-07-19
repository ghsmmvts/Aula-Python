# TUPLA
NAIPES = ('Paus', 'Copas', 'Espadas', 'Ouros')
RANKS = ('Ás', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Damas', 'Rei')

class Carta():
    def __init__(self, naipe, rank, valor):
        self.naipe = naipe
        self.rank = rank
        self.valor = valor

    # def __str__(self):
    #     return self.rank + ' de ' +  '['+str(self.valor) +']'
    
    def __str__(self):
        # f no caso é uma Template String
        return f'{self.rank} de {self.naipe} [{self.valor}]'

class Baralho():
    def __init__(self):
        self.cartas = []
 
        # Adicionar a Tupla no baralho
        for naipe in NAIPES:
            for rank in RANKS:
                carta = Carta(naipe, rank, 1)
                self.adicionar_carta(carta)

    def __str__(self):
        if len(self.cartas) == 0:
            return '[VAZIO]'

        string = ''

        for carta in self.cartas:
            string += str(carta)
            string += ', '

        return string

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def remover_carta(self):
        return self.cartas.pop()
