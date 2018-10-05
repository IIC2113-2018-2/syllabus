# Tarea 2

## Objetivos

* Detectar y aplicar patrones de diseño para resolver problemas computacionales.
* Aplicar sintaxis **UML 2.0** para definir la estructura de código de un sistema de _software_.

## Introducción

John (también conocido como _Papa_ entre sus amigos) quiere abrir un restaurante de pizzas. Como tiene mucha confianza en que su proyecto será un éxito, le ha encargado a su grupo que lo ayude con la implementación de un software para gestionar los pedidos. La idea de este programa es que imprima las instrucciones para preparar los distintos tipos de pizzas que ofrece el local, para que así cualquier persona las pueda preparar.

En las siguientes secciones de este documento se listan los requisitos que debe satisfacer su aplicación. Si este documento es ambiguo en algún contenido, pueden pedir una aclaración a través de la página de [_issues_](https://github.com/IIC2113-2018-2/syllabus/issues) del curso. Además, cualquier mejora y/o supuesto que realicen debe ser justificado en los documentos que entreguen.

Se les pide realizar en equipos de exactamente 3 personas una aplicación por consola (_command-line interface_) que permita realizar las siguientes funcionalidades.

## Requisitos funcionales

La empresa vende distintos tipos de pizzas, que se diferencian a partir de los elementos que la componen. Una pizza puede tener solamente un tipo de masa, salsa y queso, pero todos los ingredientes que el cliente quiera. Además, el proceso para preparar una orden es bastante similar entre estas:

1. Listar y preparar los ingredientes para armar la pizza
2. Hornear la pizza por 10 minutos a 180 ºC
3. Cortar la pizza en 8 pedazos
4. Empaquetar el pedido en su caja para ser enviado y adjuntar la boleta

Por simplicidad puede asumir que todas las ordenes contienen exactamente una pizza de un solo tamaño.

Cada masa, salsa, queso e ingrediente tiene un precio asociado que se detalla a continuación:

### Masas

Nombre       | Precio
------------ | -------
Tradicional  | 2000       
A la piedra  | 2000
Calzone      | 2400
Cruda        | 1700

### Salsas

Nombre  | Precio
------- | -------
Tomate  | 2000       
Blanca  | 2200
BBQ     | 2400

### Quesos

Nombre       | Precio
------------ | -------
Mozzarella   | 2000       
Reggiano     | 2200
Gouda        | 1800

### Ingredientes

Nombre              | Precio
------------------- | -------
Aceitunas negras    | 900       
Carne               | 1500
Cebolla             | 800
Champiñones         | 1000
Extra queso         | 1500
Jamón               | 1300
Palta               | 2000
Pepperoni           | 1500
Piña                | 1000
Pollo               | 1300
Salchicha           | 1000
Tocino              | 1400
Tomate              | 800

Además, algunos componentes tienen particularidades que cambian el modo de preparación de la orden:

* Masa a la piedra:
  * aumenta el tiempo de hornear en 5 minutos
* Masa calzone:
  * la pizza no se corta, se enrolla en si misma
  * se utiliza una caja especial para este tipo de pizza
* Masa cruda:
  * independiente de los ingredientes que tenga, no se hornea ni se corta, ya que el cliente la terminará de preparar
  * se utiliza una caja especial para este tipo de pizza
* Tocino:
  * aumenta el tiempo de horneado en 3 minutos
* Piña:
  * disminuye la temperatura de cocción en 20 ºC
* Palta:
  * no se agrega en la etapa de preparación, sino que al momento de empaquetar se adjunta en un embase especial

Por otra parte, como todo restaurante la pizzería tiene pizzas predefinidas a un precio conveniente, pero a estas pizzas no se les puede hacer ninguna modificación (aunque sí se les puede agregar más ingredientes). Estas pizzas son:

Nombre           | Masa            | Salsa       | Queso      | Ingredientes                                           | Precio
---------------- | --------------- | ----------- | ---------- | ------------------------------------------------------ | ------
Campesina        | A la piedra     | Blanca      | Guouda     | Pollo / Champiñones / Extra queso                      | 8800
Doble pepperoni  | Tradicional     | Tomate      | Mozzarella | Doble pepperoni / Extra queso                          | 9500
Hawaiana         | Tradicional     | Tomate      | Mozzarella | Jamón / Tomate / Champiñones / Piña             | 9000
Italiana         | Tradicional     | Tomate      | Mozzarella | Pepperoni / Salchicha / Aceitunas negras / Champiñones | 9200
Vegetariana      | A la piedra     | Blanca      | Reggiano   | Aceitunas negras / Cebolla / Tomate                    | 7900

Se espera que un usuario de su programa pueda ingresar un pedido (ya sea desde una pizza predefinida o una hecha a medida), para que luego se imprima en pantalla todas las intrucciones para realizar el pedido y el precio final de este.

## Requisitos no funcionales

* **RNF1:** Deben incluir un _README.md_ que indique los pasos para ejecutar la aplicación. **Es responsabilidad de cada alumno asegurarse que se incluya todo lo necesario para la corrección de la tarea**, de manera que todos los RF puedan probarse solo con leer la documentación (_i.e._ sin tener que revisar el código fuente ni agregar archivos al proyecto).

* **RNF2:** Deben respetar buenas prácticas de _git_ (revisar [esta guía](https://github.com/IIC2113-2018-2/syllabus/wiki/How-to-Git)):

  * *Commits* con nombres descriptivos.
  * *Commits* atómicos, es decir, responsabilidades claras y separadas.
  * *Commits* en inglés.
  * Respetar un _workflow_ definido por ustedes.


* **RNF3:** Deben desarrollar la aplicación en Python 3.7.0.

* **RNF4:** Deben utilizar una **guía de estilo** (se recomienda que se apoyen a través de _linters_). Además, deben adjuntar la configuración utilizada en el proyecto. Algunas alternativas son:

  * [Guía de Estilo](https://www.python.org/dev/peps/pep-0008/)
  * [Linter](https://www.pylint.org/)


* **RNF5:** Deben implementar como mínimo 3 adaptaciones de patrones de diseño GoF. Para cada patrón utilizado, deben incluir una explicación y justificación del diseño, detallando qué clases participan en la implementación de cada patrón.

* **RNF6:** Deben realizar un diagrama de clases UML2 (**se evaluará su correcta sintaxis**) que refleje el diseño de su aplicación y la interacción de los patrones de diseño detectados. Para lo anterior, pueden utilizar [draw.io](https://www.draw.io/), u otra aplicación del mismo estilo.

Pueden (y se recomienda) utilizar librerías, módulos y/o servicios con el fin de externalizar complejidad del programa. Sin embargo, deben validar a través de las _issues_ del curso si es una dependencia permitida.

## Inscripción grupos

Para inscribir un grupo de trabajo, uno de los integrantes deberá contestar [la siguiente encuesta](https://goo.gl/forms/VgeWE4o1x1ZsIXRP2) con los usuarios de GitHub de cada integrante. Las personas que no pertenezcan a un grupo antes del día **martes 09 de octubre a las 21:59**, serán aleatoriamente asignados a uno.

## Entrega

La entrega de cada grupo será a través del repositorio que se les haya asignado para esta tarea. Para la corrección se considerará el último _commit_ a la _branch master_ hasta el día **viernes 19 de octubre a las 23:59**.

Si se entrega la tarea atrasada se tendrá un descuento **inicial** de 5 décimas hasta un descuento de 20 décimas a las 48hrs de atraso del plazo establecido de manera lineal, con la fórmula:

### <center>5 + 15t / 48</center>

Donde `t` está en horas (es una función **continua** y no discreta) y no se permiten entregas pasadas las 48 hrs de la hora inicial de entrega.

## Política de integridad académica

Los alumnos de la Escuela de Ingeniería de la Pontificia Universidad Católica de Chile deben mantener un comportamiento acorde a la Declaración de Principios de la Universidad.  En particular, se espera que **mantengan altos estándares de honestidad académica**.  Cualquier acto deshonesto o fraude académico está prohibido; los alumnos que incurran en este tipo de acciones se exponen a un Procedimiento Sumario. Es responsabilidad de cada alumno conocer y respetar el documento sobre Integridad Académica publicado por la Dirección de Docencia de la Escuela de Ingeniería (disponible en SIDING).

**En particular, si un alumno copia un trabajo, o si a un alumno se le prueba que compró o intentó comprar un trabajo, obtendrá nota final 1.1 en el curso y se solicitará a la Dirección de Docencia de la Escuela de Ingeniería que no le permita retirar el curso de la carga académica semestral.**

Por _copia_ se entiende incluir en el trabajo presentado como propio, partes hechas por otra persona.  **En caso que corresponda a _copia_ a otros alumnos, la sanción anterior se aplicará a todos los involucrados**.  En todos los casos, se informará a la Dirección de Docencia de la Escuela de Ingeniería para que tome sanciones adicionales si lo estima conveniente.

Obviamente, está permitido usar material disponible públicamente, por ejemplo, libros o contenidos tomados de Internet, siempre y cuando se incluya la referencia correspondiente.
