# Actividad \#6

## Rúbrica

Esta actividad consiste en estudiar un _script_ escrito en Python, para luego implementar un _code refactoring_ sobre este mismo.

1. **(1,5p)** En clases, sólo se alcanzaron a ver los _smells_ de la categoría _bloaters_; esperamos que sólo mencionen los que allí aparecen. Estos son los _code smells_ a identificar.

   - **Long method:**
   Este es el más evidente de todos. El método `print_standings` tiene más de cuarenta líneas y realiza muchas operaciones que podrían ser divididas en varias secciones: extraer la información desde el archivo, cargar los partidos, inferir los equipos, calcular los puntajes, y finalmente imprimir la tabla de posiciones.

   - **Data clump:**
   Este _code smell_ aparecía en el caso de los _matches_. La terna de datos (_home_, _away_, y _score_) es utilizada de manera conjunta en distintas partes del código, como en el método `get_winner` (L20) o cada vez que se usan índices en la tupla que contiene datos del _match_ (L48, L64).

   - **Primitive obsession:**
   Relacionado con el _code smell_ anterior, puede ser visto como que el _script_ usa elementos primitivos del lenguaje (e.g. _strings_) para almacenar un _match_. También es válido afirmar que el _score_ podría ser dividido en un objeto, en vez de mantener un _string_ como `4-2`.

   - **Large class:**
   En realidad, este _code smell_ está al límite ya que `League` es una sola clase que es cohesiva en lo que hace. De todas formas, podría aparecer una vez que uno intenta solucionar el problema del _long method_. Después de hacer esto, es una buena idea separar las distintas funcionalidades en más clases.

El único _smell_ que no era aceptable era el _Long parameter list_. No hay puntos por eso.

2. **(3,0p)** Al menos debería aparecer:
   - una función para cargar los datos desde el archivo,
   - una función para obtener los puntos de un equipo,
   - una función para imprimir la tabla de posiciones,
   - una clase para guardar información de un _match_.

También se agradecen las funciones de utilidad intermedias, como para el manejo de _strings_.

3. **(1,5p)** Estas técnicas tenían que sacarlas desde
[acá](https://refactoring.guru/refactoring/techniques).
Lo importante es que solucionen los tres _code smells_ identificados en la primera parte. Aquí pueden aparecer muchas técnicas. Una que los alumnos probablemente deberían mencionar es, por ejemplo, _Extract method_ para solucionar el _Long method_.
