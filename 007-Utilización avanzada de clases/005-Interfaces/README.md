# Interfaces

## Introducción

Una interfaz es un contrato que especifica qué métodos debe implementar una clase, sin especificar cómo se implementan. Las interfaces permiten definir comportamientos esperados que múltiples clases pueden implementar de formas diferentes, promoviendo el polimorfismo y la desacoplación entre componentes del sistema.

## Aspectos Técnicos

- **Contrato de Métodos**: Define la firma de métodos que deben implementarse.
- **Implementación Múltiple**: Una clase puede implementar múltiples interfaces.
- **Métodos Abstractos**: Todos los métodos en una interfaz son implícitamente abstractos.
- **Sin Estado**: Tradicionalmente, las interfaces no contienen atributos.
- **Type Hints**: Las interfaces sirven para especificar tipos esperados en funciones.
- **Polimorfismo de Interfaz**: Diferentes clases pueden implementar la misma interfaz de formas distintas.
- **Desacoplación**: El código que usa la interfaz no necesita conocer la implementación concreta.

## Para qué Sirve

- Definir comportamientos que múltiples clases no relacionadas deben implementar.
- Permitir código genérico que trabaja con cualquier clase que implemente una interfaz.
- Facilitar testing mediante mocks e implementaciones de prueba de interfaces.
- Promover el principio "Program to interfaces, not implementations".
- Lograr mayor flexibilidad y mantenibilidad al desacoplar dependencias.
- Comunicar claramente qué comportamientos se espera que tenga un objeto.

## Conclusión

Las interfaces son uno de los mecanismos más poderosos para escribir código flexible, desacoplado y mantenible. Permiten crear sistemas donde múltiples implementaciones pueden coexistir detrás de un contrato común, facilitando extensión, testing y evolución del código sin cambios disruptivos.
