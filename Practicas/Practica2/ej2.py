# Ej2. Pida al usuario 5 números y diga si estos estaban en orden decreciente, 	creciente o desordenados.

# 1. Creamos una funcion en la que añadimos 5 variables
# 2. Creamos dos if y un else 
#   2.1 Si los numeros estan en orden creciente se lo imprimirá al usuario
#   2.2 Si los numeros estan en orden decreciente se lo imprimirá al usuario
#   2.3 Sino, imprimirá que están desordenados
# 3. Creamos las 5 variables que pedirán 5 numeros al usuario
# 4. Llamamos a la funcion con las variables

def ordenes(num1, num2, num3, num4, num5):
    if num1 < num2 and num2 < num3 and num3 < num4 and num4 < num5:
        print("Orden creciente")
    if num1 > num2 and num2 > num3 and num3 > num4 and num4 > num5:
        print("Orden decreciente")
    else:
        print("Estan desordenados")

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))
num4 = int(input("Introduce un numero: "))
num5 = int(input("Introduce un numero: "))

ordenes(num1, num2, num3, num4, num5)
