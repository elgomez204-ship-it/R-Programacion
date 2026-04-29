# Características de las Bases de Datos Orientadas a Objetos

## Introducción

Las BDOO preservan la estructura completa de los objetos sin descomponerlos en tablas. Permiten heterogeneidad de datos: objetos de diferentes tipos coexisten en la misma colección sin esquema rígido. Ejemplo: portales web (guardado.html) con estructuras variadas pueden almacenarse sin normalización compleja.

## Aspectos Técnicos

Los scripts Python aquí (05-procesar.py, 06-script que pregunta.py, etc.) usan Lxml para extraer datos HTML, XPath para navegar XML/HTML, y convierten JSON embebido en diccionarios Python. Ejemplo: extraer JSON de `<script>` tags, decodificar y convertir a estructuras de datos.

Transformación ETL: HTML → diccionarios Python → JSON/CSV. Los diccionarios se serializan directamente a MongoDB sin transformación adicional. En BDOO, un anuncio con ubicación, características e imágenes anidadas es un único documento; en SQL relacional requeriría múltiples tablas.

## Para Qué Sirve

Integración de datos heterogéneos de múltiples fuentes. Ciencia de datos: almacenar datos sin esquema predefinido, analizar, luego formalizar estructura. Microservicios: cada servicio maneja su propio almacén flexible sin coordinar cambios de esquema.

## Conclusión

Las características de BDOO (flexibilidad de esquema, persistencia de objetos complejos) simplifican integración de datos y análisis. Los scripts Python demuestran cómo extraer de fuentes heterogéneas y persistir sin capas de mapeo objeto-relacional complejas.
