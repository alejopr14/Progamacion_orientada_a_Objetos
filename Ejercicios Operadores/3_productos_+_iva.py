a = int(input("Ingrese el valor del producto: "))
b = int(input("Ingrese el valor del producto: "))
c = int(input("Ingrese el valor del producto: "))

iva = a * 0.19
total_a = a + iva

iva = b * 0.19
total_b = a + iva

iva = c * 0.19
total_c = a + iva

suma = total_a + total_b + total_c

print(f'El total a pagar es: {suma}')