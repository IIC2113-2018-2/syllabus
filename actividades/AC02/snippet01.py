"""
Aquí definimos una clase por cada servicio de autenticación.
Además, definimos la clase de un usuario de esta aplicación.
"""


class UberAuth:
    """
    Servicio de autenticación de Uber.
    """
    pass


class LyftAuth:
    """
    Servicio de autenticación de Lyft.
    """
    pass


class CabifyAuth:
    """
    Servicio de autenticación de Cabify.
    """
    pass


class User:
    """
    Usuario de la aplicación.
    """

    def __init__(self):
        pass

    def authenticate(self):
        """
        Este método nos permitirá autentificar al usuario.
        Sin embargo, existen varios servicios disponibles;
        luego, escribiremos algo de código por cada servicio.
        Pero... ¿es esto la mejor solución?
        """

        # Algo de código de UberAuth,
        # algo de código de LyftAuth,
        # algo de código de CabifyAuth.
        pass
