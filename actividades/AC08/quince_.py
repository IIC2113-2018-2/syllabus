"""
quince_.py

Copyright (c) 2018, Nebil Kawas García
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.
"""


from itertools import combinations
from textwrap import dedent


class Player:
    """
    Representa un jugador.
    """

    def __init__(self, name):
        self.name = name
        self.numbers = []

    @property
    def fifteen(self):
        fifteen = (c for c in combinations(self.numbers, 3) if sum(c) == 15)
        return next(fifteen, None)

    def __repr__(self):
        numbers = (str(number) for number in self.numbers)
        numbers = ', '.join(numbers) if self.numbers else '(vacío)'
        return f'{self.name:8.8} --> {numbers}'


class Game:
    """
    Representa un juego de Quince.
    """

    def __init__(self, p1, p2):
        self.round = 1
        self.p1 = Player(p1 or 'Mario')
        self.p2 = Player(p2 or 'Luigi')

    @property
    def current(self):
        return self.p1 if self.round % 2 else self.p2

    @property
    def available(self):
        return [
            number for number in range(1, 10)
            if number not in self.p1.numbers + self.p2.numbers
        ]

    @property
    def winner(self):
        return next((p for p in (self.p1, self.p2) if p.fifteen), None)

    def get_number(self):
        number = None
        while not number:
            try:
                number = int(input('¿Número? '))
            except ValueError:
                print('Error: esto no es un número válido.')
                print('Por favor, intenta de nuevo.')
                continue

            if number not in self.available:
                print(f'Error: {number} no está disponible.')
                print('Por favor, intenta de nuevo.')
                number = None
        return number

    def start(self):
        def print_header(title):
            print(dedent(f"""
            {title}
            {"=" * len(title)}

            El turno es de {self.current.name}.
            Los números disponibles son {self.available}."""))

        def print_footer():
            print(dedent(f"""
            {self.p1}
            {self.p2}
            """))

        while self.available and not self.winner:
            print_header(f'Ronda #{self.round}')
            number = self.get_number()
            self.current.numbers.append(number)
            print_footer()
            self.round += 1

        print(
            f'Hay un ganador: {self.winner.name} --> {self.winner.fifteen}'
            if self.winner else 'No hay ganador.'
        )


if __name__ == '__main__':
    Game(
        input('Escribe el nombre de P1: '),
        input('Escribe el nombre de P2: '),
    ).start()
