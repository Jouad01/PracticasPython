# Ej1: Hacer un diagrama para calcular y mostrar area de un triangulo

# 1. Creamos la funcion con las dos variables que necesitamos para la formula
# 2. Creamos una variable llamada A para tener dentro la formula para calcular un triangulo
# 3. Imprimimos el resultado
# 4. Llamamos al nombre de la función con dos numeros dentro.

def area(b, h):
    A = (b*h) / 2
    print(A)
area(23, 30)


# Ej2: Convertir grados centigrados a fahrenheit

# 1. Creamos la funcion con la variable que necesitamos para la formula de los grados
# 2. Creamos una variable llamada F para tener dentro la formula para pasar los grados
# 3. Imprimimos el resultado
# 4. Llamamos al nombre de la función con un numero dentro.

def grados(C):
    F = C*(9/5) + 32
    print(F)
grados(22)


# Ej3: Diagrama que diga si numero es par o no

# 1. Creamos el nombre de la funcion que llevará dentro 'num'
# 2. Creamos la variable num que pedirá al usuario que ingrese un numero
#   2.1 Si el numero introducido es par saltará el mensaje "Es par"
#   2.2 Sino, le dirá que "Es impar"
# 3. Llamamos al nombre de la función. Es importante introducir un número dentro

def numPar(num):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("Es par.")
    else:
        print("Es impar")
numPar(10)


# Ej4: Calcular el numero mayor de dos numeros

# 1. Creamos la funcion y introducimos dentro las dos variables que se usarán
# 2. Creamos las variables que pediran al usuario ingresar un numero
#   2.1 Si A (el primer numero) es mayor a B (el segundo numero) entonces se lo dirá por un mensaje
#   2.2 Sino, entonces B (el segundo numero) será mayor a A (el primer numero)
# 3. Llamamos a la funcion con dos números dentro. 


def numMayorMen(A, B):
    A = (int(input("Introduzca un numero: ")))
    B = (int(input("Introduzca otro numero: ")))
    if A > B:
        print(A, "Es mayor que", B)
    else:
        print(B, "Es mayor que", A)
numMayorMen(4, 8)