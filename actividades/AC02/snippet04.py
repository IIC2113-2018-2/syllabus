"""
Aquí tenemos una clase que realiza múltiples operaciones
relacionadas con una base de datos relacional.
"""


class DatabaseManager:
    """
    Administrador de base de datos.
    En este ejemplo, este administrador se encarga de:
    - abrir una nueva conexión,
    - extraer datos desde la base de datos,
    - ejecutar algún comando escrito en SQL,
    - escribir información en un archivo en un formato,
    - realizar algún tipo de backup de todos los datos.

    Asuma que esta clase realiza (todavía) más operaciones.
    """

    def open_database_connection(self):
        pass

    def fetch_data_from_database(self):
        pass

    def execute_sql_command(self):
        pass

    def write_data_to_file(self):
        pass

    def perform_backup(self):
        pass


# ¿Qué ocurriría si un cambio ocurre en el futuro?
# Por ejemplo,
# - ¿qué pasaría si hubiese un cambio en el formato esperado?
# - ¿qué pasaría si se utilizara un nuevo motor de base de datos?
# - ¿qué pasaría si se utilizara otro ORM para manejar las consultas?
