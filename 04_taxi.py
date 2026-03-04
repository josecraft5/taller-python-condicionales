# Ejercicio 4 Taxi

tarifa_base = 1.0

distancia = float(input("Ingresa la distancia recorrida en km: "))
hora = int(input("Ingresa la hora del viaje (0 a 23): "))

# Determinar horario y costo por km
if 6 <= hora <= 19:
    horario = "diurno"
    costo_km = 0.50
else:
    horario = "nocturno"
    costo_km = 0.65

# Calcular total
total = tarifa_base + (distancia * costo_km)

# Recargo si es mayor a 10 km
if distancia > 10:
    total += 2

# Mostrar resultados
print(f"Horario: {horario}")
print(f"Distancia: {distancia} km")
print(f"Total a pagar: ${total:.2f}")