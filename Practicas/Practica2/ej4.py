# Ej4. Pida al usuario tres números y un cuarto número, y compruebe si este último es divisor de los tres números primos

# 1. Creamos una funcion en la que añadimos 4 variables
# 2. Creamos un if y else
#   2.1 Si el cuarto numero es divisor del otro entonces imprime que es divisor
#   2.2 Sino, imprimirá que no lo es
# 3. Creamos las 4 variables que pedirán 4 numeros al usuario
# 4. Llamamos a la funcion con las variables

def pedirNumeros(num1, num2, num3, num4):

    if num4 % num3 == 0 and num4 % num2 == 0 and num4 % num1 == 0:
        print(num4, "Es divisor")
    else:
        print("No,", num4, "no es divisor")


num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))
num4 = int(input("Introduce un numero: "))

pedirNumeros(num1, num2, num3, num4)