# Actividad \#7

## Rúbrica

Esta actividad consiste en estudiar un _script_ escrito en Python, para luego implementar un _code refactoring_ sobre este mismo.

1. **(1,5p)** En esta clase, los alumnos vieron todas las familias de _code smells_ con excepción de _bloaters_, ya que esta fue revisada en la clase anterior. Esperamos que sólo mencionen _smells_ pertenecientes a las otras cuatro familias. Estos son los _code smells_ a identificar.

   - **Comments:**
   Este es el _smell_ más evidente de todos. Los comentarios como `# el contador parte en cero` son inútiles. También hay que eliminar los _docstrings_ que no aportan en nada, porque los nombres de los métodos ya son suficientemente autoexplicativos.

   - **Duplicate code:**
   En varias partes del _script_ existen fragmentos duplicados. Por ejemplo, esto puede verse concretamente entre los métodos `show` y `show_all`; en la lógica para borrar, hacer _check_ o _uncheck_ de una tarea; en el formato del _string_ al momento de imprimir una tarea. Esto reduce la mantenibilidad del código.

   - **Data class/Lazy class:**
   Esto se ve únicamente en la clase `Summary`, ya que lo único que hace es mantener una referencia al _string_ de la descripción de la tarea y nada más. De hecho, el _property_ definido no agrega ninguna lógica en el _getter_ o el _setter_ de este atributo. Por lo tanto, es posible justificar que es una _Data class_ ya que sólo guarda datos, pero no mantiene ningún comportamiento, o bien una _Lazy class_ ya que no almacena suficiente información para ser una clase en sí.

   - **Speculative Generality:**
   Esto se ve únicamente en la clase `DueDate`, ya que a partir del comentario podemos dedudcir que fue creada sin tener la certeza de que será utilizada en el futuro. Por lo mismo, no es correcto asignar _Dead code_ en este caso, ya que si bien apuntan al mismo concepto de tener código inútil, la diferencia reside en que se puede inferir que esta clase nunca se utilizó.

   - **Middle man:**
   Este _smell_ permite describir lo que ocurre con la clase `ItemManager`. Los métodos llamados por `GroceryList` son recibidos por este _manager_ que realmente no aporta en mucho. En efecto, estas acciones podrían ser perfectamente hechas por `GroceryList`. De todas formas, los alumnos podrían encontrar otro _smell_ para describir la relación entre `GroceryList` e `ItemManager`. Esto estará correcto únicamente si la justificación es válida.

2. **(3,0p)** Al menos debería aparecer:
   - la eliminación de todos los comentarios,
   - la desduplicación de la lógica entre `bought`, `show` y `show_all`,
   - la desduplicación de buscar por id y lanzar un error si no existe,
   - la desduplicación de `f'{item.id_:2d} -- {item.summary.text}'`,
   - la eliminación de `Summary` como clase,
   - la eliminación de `DueDate` como clase,
   - la eliminación de `ItemManager` y el traspaso de la lógica hacia `GroceryList`.


3. **(1,5p)** Estas técnicas tenían que sacarlas desde
[acá](https://refactoring.guru/refactoring/techniques).
Lo importante es que solucionen los cinco _code smells_ identificados en la primera parte. Aquí pueden aparecer muchas técnicas. Si la solución aplicada no está definida entre el conjunto de técnicas de _refactoring_, entonces mientras entreguen la descripción de lo que hicieron, está bien. Pero deben estar seguros de que realmente no existe en el catálogo.
