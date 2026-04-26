# Creación de Propiedades

## Introducción

Las propiedades son miembros especiales de una clase que combinan la funcionalidad de atributos con métodos de control. Permiten acceder y modificar los datos de un objeto de manera controlada, proporcionando una interfaz elegante y segura. Las propiedades son fundamentales para implementar el principio de encapsulación.

## Aspectos Técnicos

- **Getter/Get**: Método que permite leer el valor de una propiedad, típicamente con el prefijo `get_` o en lenguajes con soporte nativo como `@property`.
- **Setter/Set**: Método que permite escribir o modificar el valor de una propiedad, típicamente con el prefijo `set_`.
- **Validación**: Las propiedades permiten validar los datos antes de ser asignados.
- **Computadas**: Propiedades que calculan su valor basándose en otros atributos.
- **De solo lectura**: Propiedades que solo tienen getter, sin setter.
- **De solo escritura**: Propiedades que solo tienen setter (menos común).

## Para Qué Sirve

Las propiedades sirven para:

1. **Controlar acceso a datos**: Permitir solo modificaciones válidas a través de validaciones.
2. **Ocultar detalles internos**: El usuario de la clase no necesita saber cómo se almacenan los datos.
3. **Realizar acciones complementarias**: Ejecutar lógica adicional cuando se accede o modifica un valor.
4. **Mantener invariantes**: Garantizar que el objeto siempre está en un estado válido.
5. **Facilitar cambios futuros**: Cambiar la implementación interna sin afectar la interfaz pública.

## Conclusión

Las propiedades son una herramienta poderosa para crear clases seguras y mantenibles. Permiten implementar encapsulación de manera elegante y controlar completamente cómo se accede y modifica el estado del objeto, lo que resulta en código más robusto y profesional.
