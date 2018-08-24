"""
Aquí tenemos una clase que representa un editor de SVG.
"""


class SvgEditor:
    """
    Editor para dibujar en SVG (Scalable Vector Graphics).
    """

    def __init__(self):
        pass

    def draw_shape(self, shape):
        if shape.kind == 1:
            self._draw_rect()
        elif shape.kind == 2:
            self._draw_circle()
        elif shape.kind == 3:
            self._draw_ellipse()

        # O claro, también se podría usar un diccionario.

    def _draw_rect(self):
        """
        Dibuja un rectángulo.
        """
        pass

    def _draw_circle(self):
        """
        Dibuja un círculo.
        """
        pass

    def _draw_ellipse(self):
        """
        Dibuja una elipse.
        """
        pass


class Shape:
    """
    Clase que modela una figura geométrica.
    """

    def __init__(self, kind):
        self.kind = kind


class Rect(Shape):
    """
    Clase que modela un rectángulo.
    """

    def __init__(self):
        super().__init__()
        self.kind = 1


class Circle(Shape):
    """
    Clase que modela un círculo.
    """

    def __init__(self):
        super().__init__()
        self.kind = 2


class Ellipse(Shape):
    """
    Clase que modela una elipse.
    """

    def __init__(self):
        super().__init__()
        self.kind = 3
