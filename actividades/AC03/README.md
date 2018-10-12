# Actividad \#3

## Enunciado

Imaginemos que eres un emprendedor tecnológico y también un amante del vino[\*](#note).
Por lo mismo, has decidido renunciar a tu trabajo como _full-stack web developer_,
para dar tus primeros pasos en el objetivo de tu vida:
revolucionar la industria vitivinícola chilena.
Tu disruptiva idea intentará ofrecer un sistema integrado,
que permitirá hacer _queries_ sobre el estado de producción de un viñedo en particular.
Este sistema contaría con un lenguaje de consultas específico para este problema,
un _dashboard_ para visualizar estos indicadores en detalle,
y una aplicación web que permitiría realizar las consultas a las bases de datos.
Todo esto se integraría directamente con dispositivos instalados en los viñedos.
Para probar esto, decides invertir algo de dinero para adquirir unos sensores electrónicos
—estaban en oferta por el
[Día nacional del vino](https://es.wikipedia.org/wiki/Día_Nacional_del_Vino)—
que miden algunos datos fisicoquímicos (_e.g._ temperatura, humedad, nutrientes, acidez)
acerca de los vinos en producción.
Después de comprar los sensores, pudiste entender por qué estaban en oferta:
los datos son entregados únicamente en formato XML,
utilizando el sistema anglosajón de unidades.
Además, este hardware de sensores viene con una librería propia.
Después de estudiar la sobria documentación de la librería,
conseguiste notar que esta provee una interfaz que expone métodos y funciones que son,
relativamente, de bajo nivel, con respecto al proyecto que estás buscando desarrollar.
Asimismo, esta librería contiene bastantes funcionalidades que,
probablemente, no utilizarás en el futuro.

Para realizar el procesamiento y análisis de los datos que vienen desde los sensores,
decides trabajar con una incipiente librería de código abierto escrita en Python
(desarrollada por _Pykitchen Research Lab_, un organismo sin fines de lucro)
que, por el momento, sólo permite importar datos en el sistema métrico de unidades,
y que además están en formato JSON.
El propósito es ofrecer un sistema de información que abarque múltiples niveles.
Esto, sin duda, ayudará a matener un control de calidad acerca de la producción
y entregar oportunas notificaciones a los enólogos sobre esta misma.
Por consiguiente, los datos extraídos de los sensores
deben ser procesados desde distintos puntos de vista.
El objetivo es obtener información fisicoquímica según cada cepa,
según cada cuba de fermentación,
según cada barrica (de roble francés, obviamente)
y según cada bodega, donde podrían haber muchas de estas cubas o barricas.

Ahora, para una segunda fase del proyecto, estás pensando que, por motivos de seguridad,
algunas consultas sobre este sistema sólo deberían ser hechas por usuarios autorizados.
Además, has pensado en implementar un sistema de _logging_ en texto plano,
que permita saber qué usuario hizo qué consulta y cuándo fue realizada.
Por último, te gustaría registrar métricas sobre la _performance_ de tu sistema
para saber, por ejemplo, cuánto tiempo y memoria está tomando cada una de estas consultas.
La idea es desarrollar estas funcionalidades, una vez que la primera parte esté operativa.

## Instrucciones

En grupos de **exactamente tres** alumnos, resuelva los siguientes ejercicios.

1. **(4,0p)** De los siete patrones estructurales de diseño vistos en clases,
   proponga **exactamente cuatro** patrones —podrían aplicarse más—
   que podrían ser utilizados en la resolución del problema recién enunciado.
   Además, por cada uno de ellos, justifique de forma concisa
   por qué sería apropiado implementarlo en este contexto.
   Mencione ventajas de aplicarlos, utilizando los conceptos relacionados al diseño de software
   vistos en las clases anteriores.

2. **(1,5p)** De los cuatro patrones propuestos en la parte **1)**, escoja **exactamente tres**.
   Por cada uno de ellos, diseñe el diagrama de clases que entregue
   una modelación concreta de este patrón de diseño, en el contexto de este problema.

3. **(0,5p)** Por último, seleccione **exactamente uno** de los cuatro patrones propuestos.
   Comente cuáles podrían ser los aspectos negativos de aplicar este patrón en el problema.
   Indique, entonces, alguna desventaja que podría conllevar el uso de este patrón.

**Nota:** Puede realizar los supuestos que estime conveniente,
si existiese algún tipo de ambigüedad o algún aspecto que no esté definido en el enunciado.

---

<a name='note'>\*</a>
De hecho, tienes dos hijos: sus nombres son Merlot y Syrah. :wine_glass:
