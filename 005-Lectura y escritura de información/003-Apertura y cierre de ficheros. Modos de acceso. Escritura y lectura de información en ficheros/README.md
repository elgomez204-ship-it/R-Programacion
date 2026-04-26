# Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros

## Introducción

Trabajar con ficheros requiere comprender los ciclos de vida de los archivos: cómo se abren, se utilizan y se cierran correctamente. Los modos de acceso determinan qué operaciones se pueden realizar en un archivo (lectura, escritura, ambas), mientras que la lectura y escritura de información son las operaciones fundamentales de manipulación de datos.

## Aspectos Técnicos

- **Apertura de ficheros**: Crear una conexión entre el programa y el archivo, asignando un identificador o manejador.
- **Modos de acceso**:
  - Lectura (read/r): Solo leer contenido existente.
  - Escritura (write/w): Crear o sobrescribir archivo.
  - Anexión (append/a): Agregar contenido al final del archivo.
  - Lectura/Escritura (r+/w+): Ambas operaciones en el mismo archivo.
- **Lectura**: Obtener datos del archivo (línea por línea, por caracteres, bytes, etc.).
- **Escritura**: Guardar datos en el archivo (caracteres, líneas, bytes, etc.).
- **Cierre de ficheros**: Liberar recursos y asegurar que los datos se escriben en disco.
- **Manejo de errores**: Gestionar excepciones durante operaciones de archivo.

## Para Qué Sirve

La apertura, cierre y manipulación de ficheros sirve para:

1. **Acceder a datos**: Leer información almacenada previamente en disco.
2. **Guardar información**: Escribir datos nuevos o modificados en archivos.
3. **Mantener la integridad**: Asegurar que los datos se guarden completamente antes de cerrar.
4. **Liberar recursos**: Devolver al sistema los identificadores de archivo para evitar agotamiento de recursos.
5. **Controlar permisos**: Determinar qué operaciones se permiten en cada acceso al archivo.

## Conclusión

La gestión correcta de apertura, cierre y acceso a ficheros es fundamental para desarrollar aplicaciones confiables. Un manejo inapropiado puede llevar a corrupción de datos o pérdida de información. Comprender estos conceptos y aplicarlos correctamente es esencial para cualquier programador.
