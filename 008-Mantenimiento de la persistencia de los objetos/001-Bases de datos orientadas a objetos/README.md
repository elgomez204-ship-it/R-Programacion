# Bases de Datos Orientadas a Objetos

## Introducción

Las BDOO (bases de datos orientadas a objetos) almacenan objetos complejos directamente sin descomponerlos en tablas. MongoDB, la BDOO más popular, usa documentos JSON flexibles en lugar de esquemas rígidos. Esta subcarpeta documenta cómo persistir objetos en MongoDB usando PHP.

MongoDB es ideal para estructuras heterogéneas: cada documento puede tener diferente estructura sin campos nulos innecesarios. En e-commerce, un pedido físico y uno digital coexisten sin problema.

## Aspectos Técnicos

MongoDB utiliza BSON (Binary JSON) internamente. Cada documento es un objeto JSON con pares clave-valor: primitivos, objetos anidados o arreglos. La extensión PHP `mongodb` convierte automáticamente entre tipos PHP y BSON.

Las operaciones fundamentales son CRUD. Para inserción, se usa `Manager` con `BulkWrite`: crear documentos PHP, ejecutarlos de forma eficiente. Conexión con URI `mongodb://host:puerto` (localmente: `mongodb://127.0.0.1:27017`). El archivo `01-inserción.php` muestra inserción básica; `02-minimarket.php` demuestra un caso real.

Seguridad: conexiones SSL/TLS, consultas parametrizadas (previene inyecciones), autenticación con roles granulares.

## Para Qué Sirve

E-commerce, sistemas de alto rendimiento con escalabilidad horizontal (sharding), análisis de datos desde múltiples fuentes (APIs, IoT). La ausencia de esquema rígido acelera desarrollo.

## Conclusión

MongoDB ofrece persistencia orientada a objetos sin complejos ORM. Los ejemplos (inserción, minimarket, guardar con mongo) proporcionan patrones adaptables a casos diversos. Para profundizar: agregación, indexación, replicación, sharding.
