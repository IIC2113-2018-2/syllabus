"""
washed.py

Copyright (c) 2018, Nebil Kawas García
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.
"""

from itertools import count


class GroceryList:

    def __init__(self, title):
        self.title = title
        self.items = {}

    def add(self, *items):
        for item in items:
            self.items[item.id_] = item

    def remove(self, id_):
        return self.items.pop(id_, None)

    def check(self, id_):
        self[id_].bought = True

    def uncheck(self, id_):
        self[id_].bought = False

    def bought(self):
        bought = [str(item) for item in self.items.values() if item.bought]
        self.print_list(bought)

    def show(self, label=None):
        print(self.title)
        print('-' * len(self.title))

        uncompleted = [str(item) for item in self.items.values()
                       if not item.bought and label in item]
        self.print_list(uncompleted)
        print(f'\nHay {len(uncompleted)} ítem(s) en la lista.')
        print()

    def __getitem__(self, id_):
        try:
            return self.items[id_]
        except KeyError:
            raise KeyError(f'No existe un ítem con id={id_}.')

    @staticmethod
    def print_list(items):
        print('\n'.join(items) if items else '(lista vacía)')


class Item:

    counter = count(1)

    def __init__(self, summary, labels=None):
        self.id_ = next(Item.counter)
        self.summary = summary
        self.labels = labels or set()
        self.bought = False

    def __contains__(self, label):
        return not label or label in self.labels

    def __str__(self):
        return f'{self.id_:2d} -- {self.summary}'


if __name__ == '__main__':
    cheese_and_wine = GroceryList('Cheese & Wine')
    cheese_and_wine.add(
        Item('Dos botellas de vino tinto', {'importante'}),
        Item('Una botella de vino blanco'),

        Item('Un queso brie (180 g)', {'queso'}),
        Item('Un queso de cabra (150 g)', {'queso'}),
        Item('Un queso emmental (250 g)', {'queso'}),
        Item('Un queso parmesano (160 g)', {'queso'}),
        Item('Un queso roquefort (100 g)', {'queso'}),
        Item('Un queso camembert (160 g)', {'queso'}),

        Item('Almendras (250 g)', {'fruta', 'importante'}),
        Item('Avellanas (200 g)', {'fruta'}),
        Item('Pistachos (150 g)', {'fruta'}),

        Item('Una tabla para cortar queso', {'no-se-come'}),
        Item('Ocho copas', {'no-se-come', 'importante'}),
        Item('Una caja de Santa Helena', {'emergencia'}),
    )
