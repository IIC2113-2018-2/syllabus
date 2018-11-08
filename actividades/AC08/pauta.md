# Actividad \#8

## Rúbrica

Esta actividad consiste en estudiar un _script_ escrito en Python, para luego implementar un _code refactoring_ sobre este mismo. A diferencia de las actividades anteriores, ahora deben utilizar tests unitarios que permiten aumentar la confiabilidad de este proceso.

1. **(1,5p)** En esta pregunta, los alumnos simplemente tenían que mejorar el método `available` que permitía saber qué números estaban disponibles en el juego. Para lograr esto, bastaba con hacer un _list comprehension_. De hecho, no es correcto tener tres referencias a un arreglo de 9 números, ya que hay una presencia de código duplicado. Para evaluar esto se consideraron tres niveles de respuestas:

   - el método ya no pasa los tests unitarios,
   - el método sigue pasando los tests unitarios, pero no tiene una mejora substancial,
   - el método es legible y sigue pasando los tests unitarios.


2. **(1,5p)** En esta pregunta, los alumnos tenían que crear los tests unitarios del método `winner` usando `pytest`. Este método indica si hubo un ganador; si no lo hay todavía, devuelve `None`. La manera más simple era simular distintos casos, para luego comparar el nombre del jugador ganador con el valor esperado. Lo importante es evaluar que existan suficientes tests, sin redundancia entre ellos. Entre los casos a probar tienen que aparecer, **al menos**:

   - un juego vacío,
   - una victoria para cada equipo,
   - y dos `None` (uno por un juego que no ha terminado y otro que ya terminó en empate).


3. **(3,0p)** En esta pregunta, los alumnos tenían que crear el método `fifteen` que indica si un jugador tiene una opción de sumar quince con algún trío de números entre los que ya ha elegido. El código debe ser relativamente legible. Para esto, es fuertemente recomendable utilizar la función `combinations` del módulo `itertools` que viene con Python. Además, es importante que cumpla con lo pedido en el _docstring_ del método:

   > «Debe devolver 'None' si es que el jugador no ha conseguido sumar 15.  
      En caso contrario, debe devolver la combinación ganadora como tupla.»

   Además, los alumnos tenían que escribir los tests unitarios correspondientes a este método. Al igual que la pregunta anterior, se espera que existan suficientes tests, sin mucha redundancia entre ellos. Entre los casos a probar tienen que aparecer, **al menos**:

   - una lista vacía,
   - una lista con tres números que suman 15,
   - una lista con más de tres números que no sumen 15,
   - una lista con más de tres números donde algún trío suma 15,
   - una lista con que tenga un par que sume 15, pero no un trío.
