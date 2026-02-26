#Ejercicio 3 Descuento
subtotal = float(input("De cuanto es tu subtotal?: "))
tipo_cliente = input("Que cliente eres? (VIP) o (Regular)?: ").lower()

if tipo_cliente == "vip":
    descuento_numero= subtotal*0.15
    total= subtotal-descuento_numero
    porcentaje= 15
elif tipo_cliente == "regular":
    if subtotal>=100:
        descuento_numero= subtotal*0.05
        total= subtotal-descuento_numero
        porcentaje=5
    else:
        descuento_numero= 0
        total = subtotal
        porcentaje = "0"
else:
    descuento_numero=0
    total= subtotal
    porcentaje = 0
    
print("----------------------------")
print("          TICKET            ")
print("----------------------------")
print(f"subtotal:   {subtotal}")
print(f"descuento:  {descuento_numero:.2f},       {porcentaje}%")
print(f"Total:      {total}")

