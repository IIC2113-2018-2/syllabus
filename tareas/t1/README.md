# Tarea 1

## Objetivos

* Justificar decisiones de diseño en base a supuestos razonables.
* Aplicar sintaxis **UML 2** para definir un sistema de _software_ a través de distintos tipos de diagramas.
* Plasmar el diseño de un _software_ en un programa funcional.

## Introducción

Considerando la actividad 1 del curso, en la cual diseñaron una aplicación para registrar deudas (y como se aproxima el dieciocho), para esta tarea se les pedirá mejorar el diseño y desarrollar algunas de esas funcionalidades. De este modo, deberán realizar una aplicación de consola a través de la cual un sólo usuario interactuará de manera local.

En las siguientes secciones de este documento se listan los requisitos que debe satisfacer su aplicación. Si este documento es ambiguo en algún contenido, pueden pedir una aclaración a través de la página de [_issues_](https://github.com/IIC2113-2018-2/syllabus/issues) del curso. Además, cualquier mejora y/o supuesto que realicen deben ser justificado en los documentos que entreguen, siempre y cuando no contradiga lo que se haya dicho en el foro del curso.

## Requisitos funcionales

* **RF1:** Crear y eliminar personas. Una persona se identifica por su correo electrónico.

* **RF2:** Asociar y deshacer pagos/cobros entre 2 personas. Estos movimientos deben tener fecha, monto y descripción (puede considerar que solamente serán en moneda _CLP_). También, la proporción del monto correspondiente a cada persona es variable (i.e. no es necesariamente el monto de un movimento se divide 50-50).

* **RF3:** Imprimir en consola todo el historial de movimientos entre 2 personas, junto con el balance a la fecha.

* **RF4:** Crear y eliminar grupos. Un grupo se define como una agrupación de 3 o más personas.

* **RF5:** Asociar pagos a un grupo. Un pago tiene asociada una persona que realizó el pago, y X personas a las que se les prestó dinero en esa transacción. Este préstamo puede ser en distintas proporciones (por ejemplo, considerando las personas A, B y C puede ser que A pagó una cuenta que le correspondía 40% a B y 60% a C).

* **RF6:** Saldar cuentas de un grupo. La idea de esta funcionalidad es cerrar los movimientos de un grupo (i.e. que no se puedan crear o eliminar más movimientos) y que la aplicación informe las transferencias a realizar para saldar la cuenta del grupo. La cantidad de transferencias resultantes no puede ser mayor o igual a la cantidad de personas en el grupo. Esta información se debería poder consultar todas las veces que uno quiera.

* **RF7:** Importar y exportar la información del sistema en formato JSON y CSV, para así no perder la información ingresada cada vez que se cierra el programa.

## Requisitos no funcionales

* **RNF1:** Deben incluir un _README.md_ que indique la interfaz de la aplicación, y los requisitos para ejecutarla. **Es responsabilidad de cada grupo asegurarse que se incluya todo lo necesario para la corrección de la tarea**, de manera que todos los RF puedan probarse solo con leer la documentación (_i.e._ sin tener que revisar el código fuente ni agregar archivos al proyecto).

* **RNF2:** Deben respetar buenas prácticas de _git_ (revisar [esta guía](https://github.com/IIC2113-2018-2/syllabus/wiki/How-to-Git)):

  * *Commits* con nombres descriptivos.
  * *Commits* atómicos, es decir, responsabilidades claras y separadas.
  * *Commits* en inglés.
  * Respetar un _workflow_ definido por ustedes.


* **RNF3:** Deben desarrollar la aplicación en Ruby 2.5.1.

* **RNF4:** Deben utilizar una **guía de estilo** (se recomienda que se apoyen a través de _linters_). Además, deben adjuntar la configuración utilizada en el proyecto. Algunas alternativas son:

  * [Guía de Estilo](https://github.com/rubocop-hq/ruby-style-guide)
  * [Linter](https://github.com/rubocop-hq/rubocop)


* **RNF5:** Deben realizar diagramas **UML 2** (se evaluará su correcta sintaxis) que reflejen el diseño de su aplicación. Para lo anterior, pueden utilizar [draw.io](https://www.draw.io/), u otra aplicación del mismo estilo. Los diagramas requeridos son:

  * Diagrama de Casos de Uso
  * Diagrama de Actividad (puede ser más de un diagrama para representar todas las funcionalidades)
  * Diagrama de Componentes
  * Diagrama de Clases


* **RNF6:** Junto con los diagramas deben incluir una breve explicación y justificación del diseño, basada en los principios fundamentales y SOLID.

Pueden (y se recomienda) utilizar librerías, módulos y/o servicios con el fin de externalizar complejidad del programa. Sin embargo, deberán validar su uso por parte del equipo docente a través de la _issue_ creada especialmente para eso.

## Entrega

Esta tarea se realizará en grupos de exactamente 3 personas. A través de este [_link_](https://classroom.github.com/g/46LKtnUc) una persona de cada grupo debe crear un repositorio. Luego, los demás miembros de ese grupo deben ingresar al mismo _link_ y seleccionar el repositorio creado por su compañero. La entrega de cada grupo será a través del repositorio que hayan creado.

Para la corrección se considerará el último _commit_ a la _branch master_ hasta el día viernes 14 de septiembre a las 23:59.

## Entrega atrasada

Si se entrega la tarea atrasada se tendrá un descuento **inicial** de 5 décimas hasta un descuento de 20 décimas a las 48hrs de atraso del plazo establecido de manera lineal, con la fórmula:

### <center>5 + 15t / 48</center>

Donde `t` está en horas (es una función **continua** y no discreta) y no se permiten entregas pasadas las 48 hrs de la hora inicial de entrega.

## Política de integridad académica

Los alumnos de la Escuela de Ingeniería de la Pontificia Universidad Católica de Chile deben mantener un comportamiento acorde a la Declaración de Principios de la Universidad.  En particular, se espera que **mantengan altos estándares de honestidad académica**.  Cualquier acto deshonesto o fraude académico está prohibido; los alumnos que incurran en este tipo de acciones se exponen a un Procedimiento Sumario. Es responsabilidad de cada alumno conocer y respetar el documento sobre Integridad Académica publicado por la Dirección de Docencia de la Escuela de Ingeniería (disponible en SIDING).

**En particular, si un alumno copia un trabajo, o si a un alumno se le prueba que compró o intentó comprar un trabajo, obtendrá nota final 1.1 en el curso y se solicitará a la Dirección de Docencia de la Escuela de Ingeniería que no le permita retirar el curso de la carga académica semestral.**

Por _copia_ se entiende incluir en el trabajo presentado como propio, partes hechas por otra persona.  **En caso que corresponda a _copia_ a otros alumnos, la sanción anterior se aplicará a todos los involucrados**.  En todos los casos, se informará a la Dirección de Docencia de la Escuela de Ingeniería para que tome sanciones adicionales si lo estima conveniente.

Obviamente, está permitido usar material disponible públicamente, por ejemplo, libros o contenidos tomados de Internet, siempre y cuando se incluya la referencia correspondiente.
