"""
snippet02.py
"""

from collections import namedtuple
from itertools import permutations
Challenge = namedtuple('Challenge', 'player criterion')


class ChessClub:
    """
    Esta clase representa un club de ajedrez.
    """

    def __init__(self, name):
        self.name = name
        self.players = set()
        self.waiting = set()

    def register(self, player):
        self.players.add(player)
        player.club = self

    def add(self, challenge):
        self.waiting.add(challenge)

    def start_games(self):
        while self._get_matches():
            one, two = self._get_matches().pop()
            one.player.playing = two.player
            two.player.playing = one.player
            self.waiting -= {one, two}

    def __repr__(self):
        return f"{self.name} ({len(self.players)})"

    def _get_matches(self):
        pairs = permutations(self.waiting, 2)
        return [pair for pair in pairs if self._do_matchmaking(*pair)]

    @staticmethod
    def _do_matchmaking(one, two):
        return one.criterion(two.player.elo) and two.criterion(one.player.elo)


class ChessPlayer:
    """
    Esta clase representa un jugador de ajedrez.
    """

    def __init__(self, name, elo=1200):
        self.name = name
        self.elo = elo
        self.club = None
        self.playing = None

    def submit_challenge(self, criterion):
        if self.playing:
            print("You’re already playing!")
            return

        challenge = Challenge(self, criterion)
        self.club.add(challenge)

    def finish_game(self):
        self.playing = False

    def __repr__(self):
        return f"{self.name} ({self.elo})"


if __name__ == '__main__':
    iic2113 = ChessClub('Club IIC2113')
    carlsen = ChessPlayer('Carlsen', 2840)
    caruana = ChessPlayer('Caruana', 2820)
    aronian = ChessPlayer('Aronian', 2780)
    iic2113.register(carlsen)
    iic2113.register(caruana)
    iic2113.register(aronian)

    # El mejor ajedrecista de todos los tiempos.
    kawasparov = ChessPlayer('Kawasparov', 2880)
    iic2113.register(kawasparov)

    carlsen.submit_challenge(lambda elo: 2700 < elo < 2900)
    caruana.submit_challenge(lambda elo: 2700 < elo < 2850)
    aronian.submit_challenge(lambda elo: 2600 < elo < 2800)
    kawasparov.submit_challenge(lambda elo: 2800 < elo < 2920)

    iic2113.start_games()
