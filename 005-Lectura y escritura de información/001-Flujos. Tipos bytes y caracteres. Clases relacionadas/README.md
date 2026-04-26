# Flujos. Tipos bytes y caracteres. Clases relacionadas

## Introducción

Los flujos (streams) son canales de comunicación fundamentales en la entrada y salida de datos. Un flujo es una secuencia de bytes o caracteres que fluyen desde una fuente a un destino. Comprender los diferentes tipos de flujos y las clases relacionadas es esencial para trabajar con archivos, red y otras formas de entrada/salida en programación.

## Aspectos Técnicos

- **Flujo de bytes (InputStream/OutputStream)**: Maneja datos a nivel de byte, sin interpretación de caracteres.
- **Flujo de caracteres (Reader/Writer)**: Maneja datos a nivel de carácter, respetando codificaciones de caracteres.
- **Codificación de caracteres**: UTF-8, ASCII, UTF-16, etc. que determinan cómo se interpretan los bytes como caracteres.
- **Buffering**: Almacenamiento temporal de datos para mejorar el rendimiento.
- **Clases base**: `InputStream`, `OutputStream`, `Reader`, `Writer` y sus subclases especializadas.
- **Flujos decoradores**: Clases que envuelven otros flujos para añadir funcionalidad (BufferedReader, PrintWriter, etc.).

## Para Qué Sirve

Los flujos sirven para:

1. **Leer datos**: Obtener información de archivos, red, entrada estándar, etc.
2. **Escribir datos**: Guardar información en archivos, enviar por red, mostrar en consola, etc.
3. **Transformar datos**: Convertir entre diferentes formatos de codificación.
4. **Mejorar rendimiento**: Utilizar buffering para operaciones más eficientes.
5. **Procesar datos en tiempo real**: Manejar información que fluye continuamente sin cargar todo en memoria.

## Conclusión

Los flujos son la abstracción fundamental para toda operación de entrada/salida en programación. Dominar los diferentes tipos de flujos y sus clases relacionadas es crucial para trabajar efectivamente con archivos, redes y otros recursos. Una comprensión sólida de flujos es la base para desarrollar aplicaciones que interactúen con datos externos.
