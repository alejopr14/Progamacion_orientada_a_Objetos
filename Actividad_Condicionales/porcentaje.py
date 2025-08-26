#
producto = float(input("Ingrese el valor de la compra: "))

iva1 = producto * 0.19
total_iva1 = producto + iva1

if producto >= 100000:

    descuento1 = total_iva1 * 0.05
    total1 = total_iva1 - descuento1

    print(f"El valor de su producto con iva es {total_iva1}")
    print(f"El valor de su compra es {total1}")

else:

    descuento1 = total_iva1 * 0.01
    total2 = total_iva1 - descuento1

    print(f"El valor de su producto con iva es {total_iva1}")
    print(f"El valor de su compra es {total2}")

