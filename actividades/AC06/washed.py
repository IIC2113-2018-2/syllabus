"""
washed.py

Copyright (c) 2018, Nebil Kawas García
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.
"""

from collections import namedtuple
from operator import attrgetter
Rank = namedtuple('Rank', 'name points')


def remove_multiple_spaces(string):
    return ' '.join(string.split())


def split_into_three(string, lindex, rindex):
    return string[:lindex], string[lindex+1:rindex], string[rindex+1:]


class Match:
    """
    Esta clase representa un match de fútbol.
    """

    def __init__(self, home, score, away):
        self.home = home
        self.away = away
        self.score = score

    def __contains__(self, team):
        return team in (self.home, self.away)

    @property
    def winner(self):
        home, away = map(int, self.score.split('-'))
        if home == away:
            return None
        return self.home if home > away else self.away

    def get_points(self, team):
        if not self.winner:
            return 1
        return 3 * (self.winner == team)


class League:
    """
    Esta clase representa una liga de fútbol.
    """

    def __init__(self, name):
        self.name = name
        self.matches = []

    def load_data_from(self, path):
        def parse_line(line):
            hyndex = line.find('-')
            rspace = line.find(' ', hyndex)
            lspace = line.rfind(' ', 0, hyndex)
            return Match(*split_into_three(line, lspace, rspace))

        matches = (
            parse_line(remove_multiple_spaces(line))
            for line in open(path) if line.startswith('  ')
        )

        self.matches = [match for match in matches if match.score != '-']

    @property
    def teams(self):
        return set(
            getattr(match, attr)
            for match in self.matches for attr in ('home', 'away')
        )

    def get_points_of(self, team):
        return sum(
            match.get_points(team) for match in self.matches if team in match
        )

    @property
    def standings(self):
        ranks = (Rank(team, self.get_points_of(team)) for team in self.teams)
        return sorted(ranks, key=attrgetter('points'), reverse=True)

    def print_standings(self):
        for rank, team in enumerate(self.standings, 1):
            print(f'{rank:2d} -- {team.points:2d} {team.name}')


if __name__ == '__main__':
    premier_league = League('English Premier League')
    premier_league.load_data_from('epl-matches.txt')
    premier_league.print_standings()
