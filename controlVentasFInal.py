# Este es un programa para llevar un control de ventas eficiente en una feria a realizar en la Universidad americana
#Autores:Manuel Mayorga y Josue Reyes
#v.2.0

dias = 3
stands = 4
productos = 3

totalFeria = 0.0

print("Ingrese los montos de ventas para cada producto, stand y día:")

# Aqui recorremos cada día de la feria
for dia in range(1, dias + 1):
    print(f"\nDía {dia}:")
    totalPorDia = 0.0  # Contador de ventas de este día

    # Aqui recorremos cada stand del día
    for stand in range(1, stands + 1):
        print(f" Stand {stand}:")
        total_del_stand = 0.0  # Contador de ventas de este stand

        for producto in range(1, productos + 1):
            precio = float(input(f"  Precio del producto {producto}: "))
            total_del_stand += precio 

        # Aqui se muestra el total de este stand
        print(f"  → Total del stand {stand}: C${total_del_stand:.2f}")
        totalPorDia += total_del_stand  # Sumamos al día

    # Aqui se muestra el total de este día
    print(f" Total del día {dia}: C${totalPorDia:.2f}")
    totalFeria += totalPorDia  # Sumamos al total de la feria

# Aqui se muestra el total general de la feria
print(f"\nTotal de la feria: C${totalFeria:.2f}")
