# Actividad \#1

## Enunciado

No queda nada para septiembre y ya estamos _ad portas_ del dieciocho.
Un grupo de amigos del DCC —todos ellos patriotas— está nuevamente planificando qué hacer para esta fecha.
Sin embargo, ellos recuerdan que el año pasado, para esta misma instancia, tuvieron algunos incovenientes para repartir y saldar las cuentas después de este ilustre evento.
Esto ocurrió puesto que el sistema de anotar quién-pagó-qué detrás de las boletas, sumado al hecho de haber entregado la vida por los colores nacionales, logró precarios resultados.
Por lo mismo, después de las lecciones aprendidas, decidieron desarrollar una aplicación de código abierto para reemplazar el método de las boletas y mantener mismo el nivel de patriotismo. :chile:

Para cumplir con el objetivo descrito, esta aplicación multiplataforma debe permitir llevar las cuentas entre amigos.
El principal modo de uso sería entre parejas de usuarios: el sistema va almacenando, a lo largo del tiempo, qué ha pagado cada uno.
Este historial permitiría, por ejemplo, realizar un gran pago para saldar la deuda entre dos personas, en vez de múltiples transacciones pequeñas.
Además, esta aplicación debería tener la opción de enviar un correo como recordatorio hacia algún amigo deudor.

Por otra parte, esta aplicación debería ofrecer la opción de formar grupos.
Esta funcionalidad sería de utilidad para llevar las cuentas en un viaje entre amigos —claro, como una incursión patriótica de diez días.
Esta modalidad, además, tendría como ventaja el hecho de que sería posible, a través de un algoritmo, minimizar el número de transacciones después de una serie de compras.
En una primera fase, este algoritmo sería implementado con la ayuda de una librería externa;
no obstante, en el mediano plazo, se espera cambiarlo por un algoritmo _in-house_.
Por último, la aplicación debe exportar el historial de pagos en un _spreadsheet_ en formato
[CSV](https://en.wikipedia.org/wiki/Comma-separated_values),
[XLSX](https://en.wikipedia.org/wiki/Office_Open_XML)
y [ODS](https://en.wikipedia.org/wiki/OpenDocument).

Desde el punto de vista de la arquitectura, este software debe contar con un _back-end_ que contendría prácticamente toda la lógica de la aplicación.
Esta parte expondría un API que será consumida tanto por un cliente web como por aplicaciones nativas desarrolladas para Android, iOS y Windows 10 Mobile[\*](#note).
Estos clientes deben mostrar sencillas (pero fabulosas) visualizaciones que permitan, de un sólo vistazo, saber cuáles son las deudas actuales. También se espera ofrecer un sistema de notificaciones _push_.

Todo esto suena como un proyecto bastante abordable.
Sin embargo, antes de comenzar a escribir una línea de código, estos amigos recordaron las enseñanzas de _Diseño detallado de software_ y decidieron hacer bosquejos de algunos diagramas.

## Instrucciones

En grupos de **exactamente tres** alumnos, resuelva los siguientes ejercicios.

1. **(4,8p)** Diseñe los siguientes **seis** diagramas de UML 2,
   relacionados con el modelo 4+1 propuesto por Philippe Krutchen.

  - **Vista lógica:**
    - diagrama de clases del _back-end_,
    - diagrama de secuencia de los pagos dentro de un grupo,
  - **Vista de procesos:**       diagrama de actividad de los pagos dentro de un grupo,
  - **Vista de implementación:** diagrama de componentes de la aplicación,
  - **Vista física:**            diagrama de despliegue de la aplicación,
  - **Vista de escenarios:**     diagrama de casos de uso con la interacción
    entre dos usuarios de la aplicación.

2. **(1,2p)** Comente cómo se adapta cada uno de los cuatro principios fundamentales
   (_i.e._ abstracción, ocultamiento, cohesión, acoplamiento) en el contexto de esta aplicación.

**Nota:** Puede realizar los supuestos que estime conveniente,
si existiese algún tipo de ambigüedad o algún aspecto que no esté definido en el enunciado.

---

<a name='note'>\*</a>
No, es broma. Nadie tiene Windows 10 Mobile. :roll_eyes:
