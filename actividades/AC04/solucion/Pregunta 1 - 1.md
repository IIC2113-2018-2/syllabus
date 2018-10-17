#  IIC2113 - AC04 - Grupo 5

## Factory + Iterator

El problema a solucionar es de un zoologico, el cual puede tener distintos tipos de animales dependiendo del tipo de zoologico, a los cuales quieres alimentar.

Para solucionar este problema, utilizaremos el patron `Factory` para representar las unidades de Reproducción de distintos tipos de animales, tales como: equinos, felinos, caninos, bovinos, etc. Luego, cada zoologico tendrá distinitos tipos de animales sobre los cuales deberá iterar para poder alimentarlos a todos, utilizando el patrón `Iterator`

La razón de utilizar estos patrones juntos, es que separamos el problema global en dos subproblemas: el de generar diferentes tipos de animales para el zoologico, y el como alimentarlos a cada uno de ellos; ambos con la idea de poder agregar nuevos tipos de animales en el futuro.

Esto favorece en distintos aspectos en SOLID, por ejemplo para `Single Responsability`, estos patrones ayudarán a que cada elemento del zoologico este representado por clases con responsabilidad única: habría un Alimentador que solo se encarga de alimantar, y distinots Reproductores que solo se encargarán de cruzar su tipo de animal; favorece al principio `Open-Closed`, donde si queremos agregar más tipos de animales debemos crear más reproductores y no modificar los actuales, y tampoco será necesario modificar el iterador ya que es solo un tipo de animal más a alimentar; `Dependency Inversion`, donde se delega la responsablidad de como alimentar a cada animal.

En caso de no usar estos patrones, se usarían muchos condicionales para determinar que animales y como alimentarlos, y deberíamos modificar mucho código para poder efectivamente agregar nuevos tipos de animales, siendo muy propenso a errores


## Builder + Observer

El problema a solucionar es el de un sistema de seguimiento de despacho, donde se notificaría a un usuario cada etapa de avanza de su paquete.

Para solucionar este problema, utilizaremos el patron `Builder` para representar el despacho, donde el sistema conoce todas las etapas hasta llegar al usuario, como recepción de bodega, envio a local, recepción en local, envio a residencia y recepción en residencia. Además, usaríamos el patron `Observer`, donde en cada avance de etapa se notificaría al usuario.

La razón de utilizar estos patrones juntos, es que separamos el problema global en dos subproblemas: Generar distintos tipos de envio de manera extensible, y generar un sistema de notificaciones abstraido de que y como debe notificar.

Esto favorece en distintos aspectos en SOLID, para `Single Responsibility` aporta en separar las responabilidades de notificar al usuario y de realizar cada etapa del despacho; de igual forma, para `Open-Closed` y `Dependency Inverion`, donde para uso futuro podríamos agregar nuevos tipos de notificaciones o también generar diferentes tipos de despacho (por ejemplo, ser intermediarios con otra empresa y que llegue directamente a local y no pase por bodega, o bien que el cliente quiera retirarlo personalmente del local).

De no usar estos patrones, el código seria más ilegible y cada clase tendría multiples funciones. Por ejemplo, dentro del envío deberíamos realizar cada envio de notificación a los usuarios en el mismo código que se esta realizando el despacho. También, si quisieramos agregar tipos de notificación o formatos de entrega de producto se tendrían que agregar multiples condicionales que indiquen como y donde se está realizando.


