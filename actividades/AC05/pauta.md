# Actividad \#5

## Pauta

### Primer snippet: “Un sistema de mensajería”

**1. Explicación del código**
Estos son algunos ejemplos de comentarios que podrían desprenderse a partir de la lectura:
  - Este código implementa un sistema de mensajería a través de múltiples mensajeros.
  - Si un mensajero no puede entregar el mensaje, lo intentará el siguiente mensajero.
  - El código funciona con herencia: todos los mensajeros heredan el inicializador y **deben** implementar el método abstracto `send`. Luego, se emplea `super()` para reutilizar partes del código padre.
  - Cada mensajero tiene un conjunto de caracteres que puede enviar. Por ejemplo, los más básicos son `Lowergram` y `Uppergram` que sólo pueden enviar mensajes con [a-z] y [A-Z] respectivamente.
  - Si ningún mensajero puede enviar el mensaje (__e.g.__ el mensaje contiene un signo de puntuación), entonces aparece un mensaje que dice `"We’re sorry. We cannot deliver your message."`. Esto ocurre simplemente cuando el último mensajero no tiene un __siguiente mensajero__. Bueno, por algo es el último.
  - Los mensajeros pueden ser encadenados en cualquier orden una vez que son instanciados, lo que ofrece un buen nivel de flexibilidad.
  - Generalmente, los mensajeros abarcan un __superset__ del mensajero anterior. Además, es posible notar que mientras mayor es el conjunto de caracteres soportados, mayor es el precio por carácter.
  - Finalmente, a partir del orden creciente (según el precio por carácter) de los mensajeros, es posible concluir que este sistema busca reducir el costo total del mensaje enviado.

**2. Patrón de diseño a identificar**
  - **Patrón a identificar:** __Chain of responsibility__
  - **Justificación:** Al llamar al método `send`, un mensajero recibe un mensaje que debe enviar —en realidad, simplemente debe imprimir en pantalla. Sin embargo, dada la naturaleza de cada mensajero, ellos tienen ciertas restricciones de lo que pueden mandar. Por lo tanto, si uno de ellos no puede satisfacer el envío del mensaje, es turno del siguiente. __Chain of responsibility__ aparece entonces claramente en el código, porque cada mensajero puede ser considerado como un __handler__ concreto de la cadena.

**3. Potenciales ventajas**
Una versión que no implemente este patrón tendría, probablemente, una extensa serie de `if-elif-else`. Algunas ventajas que ofrece el código original con respecto a esta alternativa:
- Logra un bajo acoplamiento entre todos los mensajeros, que sólo deben saber quién es el siguiente en la línea, pero no comparten código entre ellos.
- Respeta __Single Responsibility Principle__, puesto que cada clase está autocontenida con su propia restricción y precio por carácter enviado.
- Respeta __Open/closed Principle__, ya que para crear un nuevo mensajero, sólo bastaría con crear una nueva clase, sin la necesidad de modificar la lógica del mensajero abstracto.

### Segundo snippet: “Un club de ajedrez”

**1. Explicación del código**
Estos son algunos ejemplos de comentarios que podrían desprenderse a partir de la lectura:
  - El club de ajedrez centraliza todos los desafíos provenientes de los jugadores de ajedrez.
  - Los desafíos quedan almacenados por el club, hasta que se ejecuta la función `start_games`.
  - Para lograr esto, el club genera todas las permutaciones de pares entre los desafíos.
  - Un match ocurre cuando las condiciones de ambos jugadores se satisfacen. Esto lo revisa  `_do_matchmaking`, que es un método estático e interno.
  - Una vez que sucede esto, ambos jugadores son removidos de la lista de desafíos.
  - El propósito de este código es, entonces, organizar partidas de ajedrez, a partir de criterios impuestos por cada jugador. Estos criterios están basados únicamente en rangos de Elo del rival.

**2. Patrón de diseño a identificar**
  - **Patrón a identificar:** __Mediator__
  - **Justificación:** El club de ajedrez actúa como mediador, puesto que es un objeto que permite encapsular la interacción entre todos los jugadores. De esta forma, el club logra comunicar las  —que, más concretamente, son desafíos— de los disintos jugadores. Esto se ve claramente cuando los jugadores se registran en el club y los desafíos son procesados de forma centralizada por este mismo.

**3. Potenciales ventajas**
Una versión que no implemente este patrón tendría que permitir que los jugadores de ajedrez se desafíen entre ellos, lo que rápidamente se volvería problemático. Cada uno de ellos tendría que conocer cuáles son los desafíos enviados por el resto. Algunas ventajas que ofrece el código original con respecto a esta alternativa:
- Logra un bajo acoplamiento entre los jugadores de ajedrez, puesto que ya no tienen que comunicarse entre ellos.
- Logra encapsulamiento en la lógica interna del club de ajedrez, ya que se logra __esconder__ del resto de las clases el algoritmo utilizado para armar las partidas de ajedrez.
- Relacionado al punto anterior, ofrece un buen nivel de abstracción hacia los jugadores de ajedrez. Ellos sólo se encargan de enviar el desafío, y es el club que, de forma interna, resuelve qué algoritmo utilizar para organizar las parejas.
