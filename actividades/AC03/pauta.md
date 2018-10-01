1. (4,0p) Es un punto por cada patrón identificado y justificado (i.e. mencionar ventajas según el contexto del problema).

Los cuatro patrones esperados eran:
  - Adapter: La conversión de datos (que vienen en XML en unidades imperiales) desde los sensores deben ser procesados por una librería externa que sólo puede recibir datos en JSON con unidades del SI. Por lo tanto, debería haber algún componente que se encargue de realizar aquella traducción de formatos.
  - Façade: El hardware con sensores viene con una librería externa escrita en código de bajo nivel que, además, tiene muchísimas funcionalidades que no son relevantes al problema; se podría, entonces, diseñar una interfaz que sólo se preocupe de obtener este subconjunto de funcionalidades relevantes al problema, para mantener el código limpio. Otro punto a considerar es que esta interfaz ofrezca un nivel de abstracción adecuado al contexto del problema. Por ejemplo, podría mezclar varias funciones de bajo nivel de la librería, en un método que sí haga sentido en el problema. Esto hará que el código sea más fácil de mantener.
  - Decorator: Este patrón permite extender las funcionalidades —por eso se hablaba de una segunda etapa— de algunos métodos para ofrecer temas de autorización, logging, o métricas de performance.
  - Composite: Un mismo método que permite obtener propiedades fisicoquímicas podría ser aplicado en distintos niveles. La idea era que notaran que el problema tenía una suerte de estructura jerárquica, donde una bodega podría tener cubas o barricas. No estoy tan seguro si es que es válido agregar la cepa en esta jerarquía. Al momento de crear el enunciado, lo pensé más como una etiqueta del vino.

De todas formas, si los alumnos señalan otro patrón, es completamente aceptable, mientras la justificación tenga sentido. También es importante que el razonamiento esté relacionado con los conceptos que se vieron en clases hasta ese momento: abstracción, ocultamiento, cohesión, acoplamiento, principios SOLID.

2. (1,5p) Es medio punto por cada diagrama de clases. Lo importante acá es que lleven los diagramas de clases al contexto del problema. No es válido si escriben Client o Service. Los términos genéricos de cliente o servicio no aportan precisión; hay mucha ambigüedad.

3. (0,5p) El propósito de esta pregunta es que los alumnos analicen los trade-offs de implementar alguno de los patrones.
