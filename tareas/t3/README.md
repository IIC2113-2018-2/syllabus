# Tarea 3

## Objetivos

* Desarrollar código bajo métricas exigentes.
* Realizar _tests_ unitarios.

## Introducción

En esta tarea se le pide que implemente una aplicación de consola para registrar una lista de _TODOs_. No es necesario que implemente persistencia entre sesiones diferentes de la aplicación.

## Requisitos funcionales

* **RF1:** Agregar un _TODO_ ingresando su título, fecha límite para realizarlo y una descripción.

* **RF2:** Poder agregar múltiples _TODOs_ con un sólo comando.

* **RF3:** Poder eliminar _TODOs_ de forma individual o múltiples al mismo tiempo.

* **RF4:** Agregar categorías a los _TODOs_. Las caterogorías se crean de manera dinámica y un _TODO_ puede tener más de una categoría. Puede ser que un _TODO_ no tenga una categoría asociada.

* **RF5:** Asignar un responsable para un _TODO_. De este responsable solamente interesa su correo electrónico válido. Puede ser que una tarea no tenga un responsable asociado.

* **RF6:** Agregar un estado para los _TODO_, el cual especifica si está en proceso o ya fue realizado. Por defecto todas las tareas comienzan con el estado de "en proceso".

* **RF7:** Listar todos los _TODOs_ que estén presentes en la aplicación con todos sus datos asociados. Se debe permitir al usuario que decida si quiere que la lista se ordene en base al título, su fecha de creación o su fecha límite de realización. También se debe permitir la opción de que solamente se listen los _TODOs_ que su fecha de realización haya expirado.

* **RF8:** Imprimir en consola un resumen de toda la lista de _TODOs_ presentes. Esta funcionalidad debe permitir agruparlos según diferentes criterios:
  - por encargados
  - por categorías
  - por estados

## Requisitos no funcionales

* **RNF1:** Deben incluir un _README.md_ que indique los pasos para ejecutar la aplicación. **Es responsabilidad de cada alumno asegurarse que se incluya todo lo necesario para la corrección de la tarea**, de manera que todos los RF puedan probarse solo con leer la documentación (_i.e._ sin tener que revisar el código fuente ni agregar archivos al proyecto). **Es muy importante que cumplan con este requisito, ya que ponderará más que para tareas anteriores.**

* **RNF2:** Deben respetar buenas prácticas de _git_ (revisar [esta guía](https://github.com/IIC2113-2018-2/syllabus/wiki/How-to-Git)):

  * *Commits* con nombres descriptivos.
  * *Commits* atómicos, es decir, responsabilidades claras y separadas.
  * *Commits* en inglés.
  * Respetar un _workflow_ definido por ustedes.


* **RNF3:** Deben desarrollar la aplicación en _Python 3.7.1_ e incluir un archivo `requirements.txt` para instalar sus dependencias con `pip3`.

* **RNF4:** Sin modificar la configuración inicial de cada una de las siguientes librerías se pide que:
  * el comando `pylint` no debe arrojar ningún error ni advertencia y debe tener una calificación superior a 9/10.
  * el comando `pytest` no debe arrojar errores
  * junto a la librería `pytest-cov` su aplicación debe tener un 100% de _coverage_


* **RNF5:** Se tomará en cuenta la calidad de los _tests_ generados (que incluyan todos los casos bordes y que no sean redundantes).

* **RNF6:** Deben realizar un diagrama de clases UML2 (**se evaluará su correcta sintaxis**) que refleje el diseño de su aplicación. Para lo anterior, pueden utilizar [draw.io](https://www.draw.io/), u otra aplicación del mismo estilo.

Pueden (y se recomienda) utilizar librerías, módulos y/o servicios con el fin de externalizar complejidad del programa. Sin embargo, deben validar a través de las _issues_ del curso si es una dependencia permitida.

## Entrega

Esta tarea es individual, por lo que asignará un repositorio para cada alumno. La entrega será a través del repositorio que se les haya asignado para esta tarea. Para la corrección se considerará el último _commit_ a la _branch master_ hasta el día lunes 3 de diciembre a las 23:59.

Si se entrega la tarea atrasada se tendrá un descuento **inicial** de 5 décimas hasta un descuento de 20 décimas a las 48hrs de atraso del plazo establecido de manera lineal, con la fórmula:

### <center>5 + 15t / 48</center>

Donde `t` está en horas (es una función **continua** y no discreta) y no se permiten entregas pasadas las 48 hrs de la hora inicial de entrega.

## Política de integridad académica

Los alumnos de la Escuela de Ingeniería de la Pontificia Universidad Católica de Chile deben mantener un comportamiento acorde a la Declaración de Principios de la Universidad.  En particular, se espera que **mantengan altos estándares de honestidad académica**.  Cualquier acto deshonesto o fraude académico está prohibido; los alumnos que incurran en este tipo de acciones se exponen a un Procedimiento Sumario. Es responsabilidad de cada alumno conocer y respetar el documento sobre Integridad Académica publicado por la Dirección de Docencia de la Escuela de Ingeniería (disponible en SIDING).

**En particular, si un alumno copia un trabajo, o si a un alumno se le prueba que compró o intentó comprar un trabajo, obtendrá nota final 1.1 en el curso y se solicitará a la Dirección de Docencia de la Escuela de Ingeniería que no le permita retirar el curso de la carga académica semestral.**

Por _copia_ se entiende incluir en el trabajo presentado como propio, partes hechas por otra persona.  **En caso que corresponda a _copia_ a otros alumnos, la sanción anterior se aplicará a todos los involucrados**.  En todos los casos, se informará a la Dirección de Docencia de la Escuela de Ingeniería para que tome sanciones adicionales si lo estima conveniente.

Obviamente, está permitido usar material disponible públicamente, por ejemplo, libros o contenidos tomados de Internet, siempre y cuando se incluya la referencia correspondiente.
