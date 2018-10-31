"""
tests_.py
"""

from pytest import fixture, mark
from quince_ import Game, Player


@fixture(name='new_game')
def _new_game():
    return Game('Punto', 'Rakhi')


@fixture(name='new_player')
def _new_player():
    return Player('Pytest')


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


@mark.parametrize(
    'one, two, expected', [
        ([], [], None),
        ([5], [], None),
        ([1], [2], None),
        ([1, 3, 5], [2, 4, 6], None),
        ([3, 5, 7], [4, 6], 'Punto'),
        ([9, 1, 2, 3], [5, 8, 4, 6], 'Rakhi'),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9], None),
    ]
)
def test_winner(new_game, one, two, expected):
    new_game.p1.numbers.extend(one)
    new_game.p2.numbers.extend(two)
    assert getattr(new_game.winner, 'name', None) == expected


@mark.parametrize(
    'numbers, expected', [
        ([], None),
        ([1], None),
        ([1, 2], None),
        ([1, 2, 3], None),
        ([7, 8, 9], None),
        ([3, 5, 7], (3, 5, 7)),
        ([4, 5, 6], (4, 5, 6)),
        ([1, 9, 6, 8], (1, 6, 8)),
        ([2, 9, 8, 4], (2, 9, 4)),
        ([9, 8, 7, 6, 5], None),
    ]
)
def test_fifteen(new_player, numbers, expected):
    new_player.numbers.extend(numbers)
    assert new_player.fifteen == expected
