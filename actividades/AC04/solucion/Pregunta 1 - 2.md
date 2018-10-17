# Actividad 4

### Grupo 07
### Integrantes: José Manuel Comber, Javier López, Raimundo Pérez


## Combinación 1: _Command_ + _Memento_

Imaginemos el caso de _Microsoft Word_: editor de texto que permite hacer Control+Z para revertir la última acción (aquí aparece _Command_: da la posibilidad de dar un paso atrás para recuperar el estado de la aplicación). Sin embargo, _Word_ no se queda ahí: además ofrece la opción de guardado automático: cada cierto tiempo, el archivo se guarda sin preguntarle al usuario. Esto se hace sin guardar la historia (acá aparece _Memento_: es una "foto" del estado): de cerrar el archivo y volver a abrir el guardado, no podremos hacer Control+Z para ir hacia atrás.

Si bien sería posible implementar todo con _Command_, esto sería sumamente caro en términos de recursos: abrir un archivo que se ha editado durante meses podría resultar insufriblemente lento. Además el código podría ser difícil de mantener, al hacer que el guardado, la apertura y cierre de archivos sea innecesariamente compleja: se logra abstracción sobre detalles que no resultan relevantes para el caso de uso regular de un usuario de la aplicación. Además se reduce el acoplamiento, al no importar la implementación de el Control+Z para el guardado, apertura y cierre de archivos. Esta última característica solo puede lograrse aplicando estos dos patrones de manera simultánea: en otro caso se sacrificaría experiencia de usuario o el bajo acoplamiento del código.


## Combinación 2: _Singleton_ + _Observer_

Imaginemos que tenemos un juego donde tenemos una entidad que corresponde a tu personaje. Este tiene muchos atributos: nombre, puntos de vida, puntos de maná, armadura, etc. Además habrán otros componentes de carácter gráfico que dependen de los atributos de este personaje: cada vez que este recibe un ataque o una poción que recupera vida, el componente que hace el _render_ de la _health bar_ debe ser notificado, para poder mostrar el cambio (ahí aparece _Observer_). Así también puede ocurrir que, si el personaje se prueba una nueva armadura, el componente encargado de mostrar visualmente al personaje debe recibir dicha información. O incluso componentes de la lógica del juego: si tienes pocos puntos de vida te podrían aparecer más pociones para recuperar vida. 

Por otra parte, es relevante que este usuario sea solo una instancia (ahí aparece _Singleton_), ya que si se tuvieran más podrían llegarle varias notificaciones a los componentes gráficos para actualizarse, lo que puede ser muy costoso.  Además puede generar problemas estilo "gato de Schrödinger": ¿qué ocurre si se duplica un personaje y solo uno muere? También puede ocurrir que cada componente no quiera guardar como atributo la referencia al personaje, sino que prefieran instanciarlo localmente (en scope de la función relevante), a sabiendas que solo va a haber una instancia.

Podrían ahorrarse muchos recursos de computación al no hacer _polling_ ni actualizaciones innecesarias. Además, de crearse un nuevo componente gráfico o lógico que requiera información de cambios del personaje, podrá extenderse fácilmente sin modificar la base de código existente (_Open-Closed Principle_). 

Podrían evitarse muchos problemas de regresión utilizando _Singleton_. Este patrón logra abstraer y ocultar parte de la lógica de la creación (el constructor es privado) y mantención del personaje, al limitar su cardinalidad. Además se previenen problemas de acoplamiento, ya que los _observers_ dependen de un solo estado: el que es notificado por la única instancia de personaje; y porque pueden haber observadores de naturaleza gráfica y otros correspondientes a la lógica del juego. Tiene sentido implementar los dos patrones simultáneamente: los observadores tendrán la confianza para llamar al observado (quizás intentando instanciarlo) sin arriesgar la coherencia del juego.
