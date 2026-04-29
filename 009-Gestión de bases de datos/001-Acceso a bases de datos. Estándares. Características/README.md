# Acceso a Bases de Datos. Estándares. Características

## Introducción

Estándares de acceso (ODBC, JDBC, PDO, mysqli) normalizan comunicación entre aplicaciones y RDBMS. Permiten cambiar entre MySQL, PostgreSQL, SQLite sin modificar lógica. El acceso incorrecto causa vulnerabilidades de seguridad: inyección SQL es el ataque más común cuando se concatenan strings en SQL.

## Aspectos Técnicos

**PHP**: `mysqli` (patrón en `09-mysql desde mysqli.php`) es seguro con prepared statements: `mysqli_prepare()` + `mysqli_stmt_bind_param()` + `mysqli_stmt_execute()`. PDO es un layer de abstracción multiplataforma. Establecer charset con `mysqli_set_charset()` para evitar problemas de codificación.

**Python**: `sqlite3` (módulo estándar) almacena datos en archivo local. Prepared statements nativos: `cursor.execute("SELECT * FROM usuarios WHERE id = ?", (1,))`. Desde Python a MySQL usa `PyMySQL` o connectors oficiales.

**Seguridad**: Usar prepared statements previene inyecciones SQL. Nunca hardcodear credenciales (usar variables de entorno). SSL/TLS para conexiones remotas. Permisos granulares: usuarios específicos con solo permisos necesarios.

## Para Qué Sirve

Web: bridging entre UI (HTML/JS) y datos. Data science: extraer y analizar datos con Pandas, NumPy. Portabilidad: cambiar RDBMS sin reescribir aplicación.

## Conclusión

Principios clave: conexiones gestionadas, prepared statements, manejo de errores, cierre de recursos. Inyección SQL es común porque desarrolladores no dominan estos principios básicos. Luego resolver problemas complejos.


