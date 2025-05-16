# Programa que registra el estado de uso de computadoras en dos laboratorios
# Cada laboratorio tiene 5 filas con 4 computadoras

# Contadores para el laboratorio 1
ocupadas1 = 0
libres1 = 0

# Laboratorio 1
print("Llenando datos del Laboratorio 1")
for fila in range(1, 6):  # 5 filas
    for col in range(1, 5):  # 4 columnas
        estado = int(input(f"Fila {fila} Columna {col}: Ingrese 1 si está ocupada o 0 si está libre: "))
        if estado == 1:
            ocupadas1 += 1
        else:
            libres1 += 1

# Contadores para el laboratorio 2
ocupadas2 = 0
libres2 = 0

# Laboratorio 2
print("Llenando datos del Laboratorio 2")
for fila in range(1, 6):  # 5 filas
    for col in range(1, 5):  # 4 columnas
        estado = int(input(f"Fila {fila} Columna {col}: Ingrese 1 si está ocupada o 0 si está libre: "))
        if estado == 1:
            ocupadas2 += 1
        else:
            libres2 += 1

# Mostrar los resultados finales
print("Resumen del Laboratorio 1:")
print("Ocupadas:", ocupadas1)
print("Libres:", libres1)

print("Resumen del Laboratorio 2:")
print("Ocupadas:", ocupadas2)
print("Libres:", libres2)