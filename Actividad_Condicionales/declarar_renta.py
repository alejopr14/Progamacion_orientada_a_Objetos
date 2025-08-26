edad = int(input("Por favor ingrese su edad: "))
ingresos = int(input("Ingrese el valor de sus ingresos mensuales: "))

if (edad >= 18) and (ingresos >= 5000000):
    print("Tiene que declarar renta")
else:
    print("No declara renta")
