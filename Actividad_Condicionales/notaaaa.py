nota1 = int(input("Ingresa tu primera nota: "))
nota2 = int(input("Ingresa tu segunda nota: "))
nota3 = int(input("Ingresa tu tercera nota: "))

suma = nota1 + nota2 + nota3
promedio = suma / 3

if promedio < 3:
    print ("Reprobaste culero")
elif ( promedio >= 3 ) and ( promedio <= 4):
    print ("Aprobo")
elif (promedio >= 41) and (promedio <= 45):
    print("Excelente")
elif (promedio >= 46) and (promedio <= 50):
    print("Felicitaciones")
else:
    print ("Nota no valida")