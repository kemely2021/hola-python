# Ejercicio 1: Calculadora básica
# - Pide al usuario dos números
# - Muestra suma, resta, multiplicación y división
# - Controla la división entre cero

n1 = float(input("Numero 1:"))
n2 = float(input("Numero 2:"))

if n2 != 0:
	print("Suma",n1+n2)
	print("Resta",n1-n2)
	print("Multiplicacion",n1*n2)
	print("Division",n1/n2)
else:
	print("No se puede dividir entre 0")
