"""
tests.py
"""

from pytest import fixture, mark
from quince import Game


@fixture(name='new_game')
def _new_game():
    return Game('Punto', 'Rakhi')


@mark.parametrize(
    'one, two, expected', [
        ([], [], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8], []),
        ([1, 2], [3, 4], [5, 6, 7, 8, 9]),
        ([3, 2, 1], [9, 8, 7], [4, 5, 6]),
    ]
)
def test_available(new_game, one, two, expected):
    new_game.p1.numbers.extend(one)
    new_game.p2.numbers.extend(two)
    assert new_game.available == expected


def test_winner():
    pass


def test_fifteen():
    pass
