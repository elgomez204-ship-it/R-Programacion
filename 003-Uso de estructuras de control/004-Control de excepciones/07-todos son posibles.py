dividendo = 4
divisor = 0

try:
    division = dividendo / divisor

except ZeroDivisionError:
    print("❌ Error: división por cero.")

except TypeError:
    print("❌ Error: tipos de datos incompatibles para la operación.")

except ValueError:
    print("❌ Error: valor no válido.")

except NameError:
    print("❌ Error: variable no definida.")

except IndexError:
    print("❌ Error: índice fuera de rango.")

except KeyError:
    print("❌ Error: clave inexistente en un diccionario.")

except AttributeError:
    print("❌ Error: atributo no encontrado en el objeto.")

except ImportError:
    print("❌ Error: problema al importar un módulo o función.")

except FileNotFoundError:
    print("❌ Error: archivo no encontrado.")

except PermissionError:
    print("❌ Error: permiso denegado al acceder a un recurso.")

except OSError:
    print("❌ Error del sistema operativo (archivos, rutas, etc.).")

except MemoryError:
    print("❌ Error: la memoria disponible se ha agotado.")

except RecursionError:
    print("❌ Error: recursión demasiado profunda.")

except Exception as e:
    print("⚠️  Error inesperado:")
    print(type(e).__name__, "-", e)

except BaseException as e:
    print("🛑 Error crítico del sistema:")
    print(type(e).__name__, "-", e)

else:
    print("✅ La operación se realizó correctamente.")

finally:
    print("🔚 Fin del bloque try-except.")