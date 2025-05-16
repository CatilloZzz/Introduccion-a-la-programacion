# Definición de parámetros
dias = 3
stands = 4
productos = 3

# Acumulador general de la feria
total_feria = 0.0

print("Ingrese los montos de ventas para cada producto, stand y día:")

# Recorremos cada día de la feria
for dia in range(1, dias + 1):
    print(f"\nDía {dia}:")
    total_por_dia = 0.0  # Contador de ventas de este día

    # Recorremos cada stand del día
    for stand in range(1, stands + 1):
        print(f" Stand {stand}:")
        total_del_stand = 0.0  # Contador de ventas de este stand

        # Recorremos cada producto del stand
        for producto in range(1, productos + 1):
            precio = float(input(f"  Precio del producto {producto}: "))
            total_del_stand += precio  # Sumamos al stand

        # Mostramos el total de este stand
        print(f"  → Total del stand {stand}: C${total_del_stand:.2f}")
        total_por_dia += total_del_stand  # Sumamos al día

    # Mostramos el total de este día
    print(f" Total del día {dia}: C${total_por_dia:.2f}")
    total_feria += total_por_dia  # Sumamos al total de la feria

# Mostramos el total general de la feria
print(f"\nTotal de la feria: C${total_feria:.2f}")