"""
smelly.py

Me pidieron que escribiera un _script_ para manejar una lista de compras.
Eso sí, no estoy cachando bien cómo funciona esta versión de HackerRank.
Aunque, según escuché por ahí, le llaman “editor de texto”. Tela igual.

                                               -- un alumno de IIC1103
"""

from datetime import date


class GroceryList:

    def __init__(self, title):
        self.title = title
        self.manager = ItemManager()  # así como el CEO de la clase

    def add(self, *items):
        for item in items:
            self.manager.add_item(item)

    def remove(self, id_):
        self.manager.remove_item(id_)

    def check(self, id_):
        self.manager.check_item(id_)

    def uncheck(self, id_):
        self.manager.uncheck_item(id_)

    def bought(self):
        something = False
        for item in self.manager.items.values():
            if item.bought == True:
                print(f'{item.id_:2d} -- {item.summary.text}')
                something = True

        if something == False:
            print('(lista vacía)')

    def show(self, label):
        counter = 0  # el contador parte en cero
        for item in self.manager.items.values():
            if item.bought == False:
                if label is None:
                    print(f'{item.id_:2d} -- {item.summary.text}')
                    counter += 1
                elif label in item.labels:
                    print(f'{item.id_:2d} -- {item.summary.text}')
                    counter += 1

        if counter == 0:
            print('(lista vacía)')
        else:
            print(f'\nHay {counter} ítem(s) en la lista.')
        print()

    def show_all(self):
        print(self.title)
        print('-' * len(self.title))

        counter = 0  # el contador parte en cero
        for item in self.manager.items.values():
            if item.bought == False:
                print(f'{item.id_:2d} -- {item.summary.text}')
                counter += 1  # Esto es lo mismo que “counter = counter + 1”
                              # pero hoy igual me siento hacker po' compadre.

        if counter == 0:
            print('(lista vacía)')
        else:
            print(f'\nHay {counter} ítem(s) en la lista.')
        print()


class ItemManager:

    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.id_] = item

    def remove_item(self, id_):
        """
        Este método permite sacar un ítem de la lista de compras.
        Esto es clave porque, a veces, puedes cambiar de opinión.
        A veces, quieres comprar algo, pero después te arrepientes.
        Por ejemplo, la semana pasada, yo quería comprar una tarea.
        Pero mis amigos igual le dieron color. No me bancaron nada.
        Perro, yo sólo quería aumentar el empleo y el PIB en Chile.
        """

        if id_ in self.items.keys():
            del self.items[id_]
        else:
            raise KeyError(f'Sorry perro, no existe un ítem con id={id_}.')

    def check_item(self, id_):
        if id_ in self.items.keys():
            self.items[id_].bought = True
        else:
            raise KeyError(f'Sorry perro, no existe un ítem con id={id_}.')

    def uncheck_item(self, id_):
        if id_ in self.items.keys():
            self.items[id_].bought = False
        else:
            raise KeyError(f'Sorry perro, no existe un ítem con id={id_}.')


class Item:

    counter = 0

    def __init__(self, summary, labels=None):
        Item.counter += 1
        self.id_ = Item.counter

        self.bought = False
        self.summary = Summary(summary)

        if labels is None:
            self.labels = set()
        else:
            self.labels = labels


class Summary:

    def __init__(self, text):
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


class DueDate:
    """
    En realidad, esta clase es para modelar una futura funcionalidad.
    """

    def __init__(self, datestr):
        year, month, day = datestr.split('-')
        self.due_date = date(int(year), int(month), int(day))


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
        # Nota: el código huele peor que este último queso.

        Item('Almendras (250 g)', {'fruta', 'importante'}),
        Item('Avellaas (200 g)', {'fruta'}),
        Item('Pistachos (150 g)', {'fruta'}),

        Item('Una tabla para cortar queso', {'no-se-come'}),
        Item('Ocho copas', {'no-se-come', 'importante'}),
        Item('Una caja de Santa Helena', {'emergencia'}),
    )
