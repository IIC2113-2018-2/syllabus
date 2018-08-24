"""
Aquí tenemos dos clases: un tablero bidimensional y otro tridimensional.
"""


class Board:
    """
    Tablero bidimensional.
    """

    def __init__(self, height, width, tiles):
        self.height = height
        self.width = width
        self.tiles = tiles

    def add_piece(self, x, y):
        pass

    def remove_piece(self, x, y):
        pass


class ThreeDimBoard(Board):
    """
    Tablero tridimensional.
    """

    def __init__(self, height, width, tiles, depth):
        super().__init__(height, width, tiles)
        self.depth = depth

    def add_piece(self, x, y, z):
        pass

    def remove_piece(self, x, y, z):
        pass
