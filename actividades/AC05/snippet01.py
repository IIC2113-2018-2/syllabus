"""
snippet01.py
"""

import abc
from string import ascii_lowercase, ascii_uppercase, ascii_letters


class Telegram(abc.ABC):
    """
    Este mensajero sólo permite enviar mensajes abstractos.
    """

    def __init__(self, messenger=None):
        self.next_ = messenger

    @abc.abstractmethod
    def send(self, message, capability):
        if capability:
            print(f"Message:\n{message}\n")
            cost = len(message) * self.PRICE_PER_CHAR
            print(f"-- Sent by {self.__class__.__name__} Messenger")
            print(f"-- For a total cost of only {cost} nebcoins.\n")

        elif self.next_:
            self.next_.send(message)

        else:
            print("We’re sorry. We cannot deliver your message.")


class Lowergram(Telegram):
    """
    Este mensajero sólo permite enviar texto en minúsculas.
    """

    PRICE_PER_CHAR = 2

    def send(self, message, capability=None):
        lower = set(ascii_lowercase)
        super().send(message, all(char in lower for char in message))


class Uppergram(Telegram):
    """
    Este mensajero sólo permite enviar texto en mayúsculas.
    """

    PRICE_PER_CHAR = 3

    def send(self, message, capability=None):
        upper = set(ascii_uppercase)
        super().send(message, all(char in upper for char in message))


class Asciigram(Telegram):
    """
    Este mensajero sólo permite enviar texto en ASCII.
    """

    PRICE_PER_CHAR = 4

    def send(self, message, capability=None):
        letters = set(ascii_letters)
        super().send(message, all(char in letters for char in message))


class Alphagram(Telegram):
    """
    Este mensajero sólo permite enviar texto alfabético.
    """

    PRICE_PER_CHAR = 5

    def send(self, message, capability=None):
        super().send(message, message.isalpha())


class AlphagramPlus(Telegram):
    """
    Este mensajero sólo permite enviar texto alfabético con espacios.
    """

    PRICE_PER_CHAR = 7

    def send(self, message, capability=None):
        super().send(message, message.replace(' ', '').isalpha())


class AlnumgramPlus(Telegram):
    """
    Este mensajero sólo permite enviar texto alfanumérico con espacios.
    """

    PRICE_PER_CHAR = 10

    def send(self, message, capability=None):
        super().send(message, message.replace(' ', '').isalnum())


if __name__ == '__main__':
    telegram = Lowergram(
        Uppergram(
            Asciigram(
                Alphagram(
                    AlphagramPlus(
                        AlnumgramPlus())))))

    telegram.send('electroencefalografista')
    telegram.send('PascalCaseDesignPattern')
    telegram.send('DCC')
    telegram.send('IIC2113')
    telegram.send('Noutilizaréningúnespacioparaahorrarnebcoins')
    telegram.send('The quick brown fox jumps over the lazy dog')
    telegram.send('Danky Nogatongamegalosomanjarchafafrinilofo')
    telegram.send('3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2')
    telegram.send('I n s t a l l       F i r e f o x       6 2')
