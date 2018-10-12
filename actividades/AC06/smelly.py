"""
smelly.py

Disclaimer:
===========

Yo no escribo código así. Me esforcé para lograr algo tan aterrador como esto.
Le pido perdón a toda persona que tenga que descifrar que lo este código hace.
Le pido perdón a mi familia, a mis amigos y sobre todo a ti, Guido van Rossum.

                                                                     -- @nebil
"""


class League:

    def __init__(self, name):
        self.name = name

    def get_winner(self, home, away, score):
        home_, away_ = score.split('-')
        home_ = int(home_)
        away_ = int(away_)

        if home_ > away_:
            return home
        elif home_ < away_:
            return away
        else:
            return None

    def print_standings(self, path):
        matches = []
        with open(path) as file:
            for line in file:
                if line.startswith('  '):
                    line = ' '.join(line.split())
                    index = line.find('-')
                    lspace = line.rfind(' ', 0, index)
                    rspace = line.find(' ', index)
                    home = line[:lspace]
                    score = line[lspace+1:rspace]
                    away = line[rspace+1:]

                    if score == '-':
                        continue

                    matches.append((home, score, away))

        teams = set()
        for match in matches:
            teams.add(match[0])
            teams.add(match[2])

        standings = []
        for team in teams:
            its_matches = []
            for match in matches:
                if team in match:
                    its_matches.append(match)

            points = 0
            for match in its_matches:
                winner = self.get_winner(match[0], match[2], match[1])
                if winner == team:
                    points += 3
                elif winner is None:
                    points += 1
                else:
                    points += 0

            standings.append((team, points))

        sorted_ = sorted(standings, key=lambda team: team[1], reverse=True)
        for rank in range(len(sorted_)):
            print(f'{rank+1:2d} -- {sorted_[rank][1]:2d} {sorted_[rank][0]}')


if __name__ == '__main__':
    premier_league = League('English Premier League')
    premier_league.print_standings('epl-matches.txt')
