''' 
    Calculadora de cuadras
    v0.1 (c) 2026 Juan Patino
    Programa que calcula número de cuadras a partir de los perros
'''

import math as matematicas

# Datos de inicio
perros = 0
cuadras = 0
caballos_por_cuadra = 0

# Entrada de información
perros_por_cuadra = int(input("Introduce el número de perros por cuadra: "))
perros = int(input("Introduce el número de perros: "))

# Realización de cálculos
cuadras = perros / perros_por_cuadra
redondeoalza = matematicas.ceil(cuadras)

# Salida de resultados
print("Si tienes",perros,"perros")
print("Y te caben",perros_por_cuadra,"perros por cuadra")
print("En ese caso necesitas",redondeoalza,"cuadras")