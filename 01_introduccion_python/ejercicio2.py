# Ejercicio 2: Conversión de unidades
# - Pide al usuario una distancia en kilómetros
# - Convierte a millas y muestra el resultado

# Para obtener un resultado aproximado, divide el valor de longitud por 1.609

distancia = float(input("Distancia en km: "))
millas = distancia / 1.609
print("Distancia en millas:",millas)
#MEJORA OPCIONAL
print(f"Distancia en millas: {millas:2f}")