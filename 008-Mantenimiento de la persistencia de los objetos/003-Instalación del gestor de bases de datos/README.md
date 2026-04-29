# Instalación del Gestor de Bases de Datos

## Introducción

Un DBMS (gestor de bases de datos) requiere instalación y configuración correcta. Decisiones sobre rutas de datos, puertos, autenticación y logging impactan rendimiento, seguridad y estabilidad. Esta carpeta aborda conceptos esenciales usando MongoDB como referencia.

## Aspectos Técnicos

Descargar binarios de MongoDB desde el sitio oficial según SO (Windows/Linux/macOS). Configurar mongod.conf con: ruta de datos (`--dbpath`), puerto (default 27017), nivel de logging. Iniciar como servicio: `systemctl start mongod` (Linux) o servicio Windows automático.

Verificar con `netstat` (confirmar puerto), `mongosh` (conectar cliente), `show dbs` (listar bases). Autenticación: crear usuarios con `db.createUser()`. Herramientas visuales: MongoDB Compass (oficial) para explorar datos e índices. Debugging: logs en archivo, `mongostat` para estadísticas en tiempo real.

## Para Qué Sirve

Desarrollo local: base de datos funcional para experimentar sin restricciones. Debugging: acceso directo a logs, introspección de datos y diagnóstico. Optimización: decisiones sobre cache, threads, SSD vs. HDD basadas en instalación real.

## Conclusión

Instalación correcta es fundamental. Documentar con scripts para reproducibilidad. Familiarizarse con herramientas de monitoreo es crítico para diagnosticar problemas en vivo.


