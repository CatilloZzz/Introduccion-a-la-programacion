# Este es un programa para llevar un control de ventas eficiente en una feria a realizar en la Universidad americana 



DIAS = 3
STANDS = 4
PRODUCTOS = 3

total_feria = 0

print("Ingrese los montos de ventas para cada producto, stand y día:")

for dia_cont in range(1, DIAS + 1):
    print(f"\nDía {dia_cont}:")
    total_dia = 0

    for stand_cont in range(1, STANDS + 1):
        print(f" Stand {stand_cont}:")
        total_stand = 0

        for producto_cont in range(1, PRODUCTOS + 1):
            while True:
                try:
                    monto = float(input(f"  Monto producto {producto_cont}: "))
                    if monto < 0:
                        print("    Error: el monto debe ser positivo.")
                    else:
                        break
                except ValueError:
                    print("    Entrada inválida, ingrese un número.")
            total_stand += monto

        print(f"  Total Stand {stand_cont}: ${total_stand:.2f}")
        total_dia += total_stand

    print(f" Total Día {dia_cont}: ${total_dia:.2f}")
    total_feria += total_dia

print(f"\nTotal General de la Feria: ${total_feria:.2f}")
