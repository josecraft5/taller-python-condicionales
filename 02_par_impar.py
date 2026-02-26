#Ejercicio 2 Par Impar
numero = int(input("Dime un numero entero: "))
edad = int(input("Dime tu edad: "))

if numero % 2 == 0:
    numero= "PAR"
else:
    numero= "IMPAR"


if edad>=18:
    edad= "MAYOR"
else:
    edad= "MENOR"

print(f"Tu numero es {numero}")
print(f"Y eres {edad} de edad")