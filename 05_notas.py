#Ejercicio 5 notas

n1 = int(input("Cual fue la primera nota?: "))
while n1>100 or n1<0:
    n1 = int(input("Error: nota inválida, Ingrese una nota correcta: "))

n2 = int(input("Cual fue la Segunda nota?: "))
while n2>100 or n2<0:
    n2 = int(input("Error: nota inválida, Ingrese una nota correcta: "))

n3 = int(input("Cual fue la Tercera nota?: "))
while n3>100 or n3<0:
    n3 = int(input("Error: nota inválida, Ingrese una nota correcta: "))

promedio1 = n1 + n2 + n3
promedio2 = promedio1 / 3

if promedio2 >=90:
    gpa = "Excelente"
elif promedio2 >=80:
    gpa = "Muy bueno"
elif promedio2 >=70:
    gpa = "bueno"
elif promedio2 >=60:
    gpa = "supletorio"
elif promedio2>=0:
    gpa = "Reprobado"

print("=====================")
print("        D2L          ")
print("=====================")
print("Tus notas fueron:    ")
print(f"Nota 1: {n1}        ")
print(f"Nota 2: {n2}        ")
print(f"Nota 3: {n3}        ")
print("---------------------")
print(f"Tu promedio fue de: {promedio2:.2f}")
print(f"Y tu calificacion final: {gpa}")




