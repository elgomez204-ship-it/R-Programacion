munecos_por_dia = 10
total_munecos = 0

for anio in range(2000, 2026):
    for mes in range(1, 13):
        for dia in range(1, 31):
            print(f"Día {dia} del mes {mes} del año {anio}: {munecos_por_dia} muñecos fabricados")
            total_munecos += munecos_por_dia

print(f"\nTotal de muñecos fabricados en todo el período: {total_munecos}")