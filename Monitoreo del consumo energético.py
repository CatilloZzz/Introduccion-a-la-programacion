# Programa para monitorear el consumo energético de 4 edificios durante 1 semana
#Autores:Manuel Mayorga y Josue Reyes
#v.2.0


edificios = 4
dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
turnos = ("mañana", "tarde", "noche")

# Acumulador general opcional (si quieres sumar todos los edificios)
total_general = 0

print("Registro de consumo energético (kW) por edificio, día y turno\n")

# Recorremos cada edificio
for edificio in range(1, edificios + 1):
    print(f"\n--- Edificio {edificio} ---")
    total_edificio = 0 # Acumulador de consumo semanal de este edificio

    # Recorremos cada día de la semana
    for dia in dias:
        print(f"\n Día: {dia}")
        # Recorremos los 3 turnos
        for turno in turnos:
            consumo = float(input(f"  Consumo en turno {turno}: "))
            total_edificio += consumo  # Sumamos al total del edificio

    # Calculamos el promedio diario (o semanal, según se requiera)
    promedio_semanal = total_edificio / 7

    # Mostramos resultados del edificio
    print(f"\n=> Total consumido en Edificio {edificio}: {total_edificio:.2f} kW")
    print(f"=> Promedio diario (semana): {promedio_semanal:.2f} kW/día")

    total_general += total_edificio  # Para un total de todos los edificios

# Si se desea, mostrar también el total general
print(f"\n*** Consumo total de los {edificios} edificios: {total_general:.2f} kW ***")
