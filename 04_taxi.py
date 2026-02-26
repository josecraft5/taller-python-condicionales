distancia = float(input("Cual es la distancia recorrida en Km: "))
tiempo = int(input("Cual fue la hora de viaje (0-23): "))

tarifa_base = 1

while tiempo>23 or tiempo< 0:
    tiempo = int(input("Cual fue la hora de viaje (0-23): "))
    if tiempo>=6 and tiempo<=19:
        print("bien")
    else:
        print("mal")
    
