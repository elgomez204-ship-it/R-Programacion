# Utilización de Clases Heredadas

## Introducción

La herencia es uno de los pilares de la Programación Orientada a Objetos que permite crear nuevas clases basándose en clases existentes. Una clase heredada (subclase o clase derivada) hereda todos los atributos y métodos de su clase padre (superclase o clase base) y puede añadir nuevas funcionalidades o modificar las existentes. La herencia promueve la reutilización de código y permite modelar relaciones jerárquicas entre conceptos.

## Aspectos Técnicos

- **Clase base/superclase**: La clase original de la cual se hereda.
- **Clase derivada/subclase**: La nueva clase que hereda de la clase base.
- **Herencia simple**: Una clase hereda de una única clase base.
- **Herencia múltiple**: Una clase hereda de múltiples clases base (no soportada en todos los lenguajes).
- **Métodos sobrescritos**: Redefinir un método heredado en la subclase para cambiar su comportamiento.
- **Métodos abstractos**: Métodos definidos en la clase base que deben implementarse en las subclases.
- **Polimorfismo**: Usar objetos de diferentes clases derivadas a través de la interfaz de la clase base.

## Para Qué Sirve

La herencia sirve para:

1. **Reutilizar código**: Evitar duplicar código común en múltiples clases.
2. **Modelar jerarquías**: Representar relaciones "es un" entre conceptos.
3. **Facilitar extensiones**: Crear nuevas clases que extienden funcionalidad existente.
4. **Promover consistencia**: Todas las clases derivadas comparten una interfaz común.
5. **Implementar polimorfismo**: Permitir que código genérico trabaje con diferentes tipos de objetos.

## Conclusión

La herencia es un mecanismo poderoso que, cuando se usa correctamente, lleva a código más limpio, reutilizable y fácil de mantener. Sin embargo, debe usarse con cuidado, ya que una jerarquía de herencia mal diseñada puede hacer el código más complejo. La herencia es especialmente útil para modelar relaciones claras y naturales entre entidades.
