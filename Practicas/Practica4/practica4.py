# Ej1: Escribe un programa que escriba a los siguientes números (la separación entre número es para facilitar 
# cuántos números se deben escribir en cada bucle) y en el que la función range que utilices tenga un ÚNICO argumento 
# y que el valor de este se corresponda con el número de elementos que aparecen en la lista.

# 1 2 3 4 5 6 7 8 9 10
def uno():
    for i in range(1, 11):
        print(i, end=" ")
    print()
uno()

# 2 4 6 8 10 12 14 16 18 20
def dos():
    # empezar por 2 porque 1 no es par
    # 21 porque queremos que vaya hasta el 20
    # 2 porque queremos que vaya de dos en dos
    for i in range(2, 21, 2):
        print(i, end=" ")
dos()

# 10 14 18 22 26 30
def tres():
    # empezar por 10 porque es el primer numero par
    # 31 porque queremos que vaya hasta el 30
    # 4 porque queremos que vaya de cuatro en cuatro
    for i in range(10, 31, 4):
        print(i, end=" ")
tres()

# 20 22 24 26 28 30 32 34 36 38
def cuatro():
    # empezar por 20 porque es el primer numero par
    # 39 porque queremos que vaya hasta el 38
    # 2 porque queremos que vaya de dos en dos
    for i in range(20, 39, 2):
        print(i, end=" ")
cuatro()

# 40 35 30 25 20 15 10 5 0
def cinco():
    # empezar por 40 porque es el primer numero par
    # -1 porque queremos que vaya hasta el 0
    # -5 porque queremos que vaya de cinco en cinco
    for i in range(40, -1, -5):
        print(i, end=" ")
cinco()



# Ej2: Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares

def numPar():
    num1 = int(input("Escribe un número: "))
    num2 = int(input(f"Escribe un número mayor que {num1}: "))
    # for para recorrer todos los números entre num1 y num2. num2 + 1 porque el range no incluye el último número
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print("El número " + str(i) + " es par")
        else:
            print("El número " + str(i) + " es impar")
numPar()

# Ej3: Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.

# Dame un número: 30
# Dame otro número mayor que 30: 32
# La suma desde 30 hasta a 32 es: 93
# 30+31+32 = 93

def suma():
    num = int(input("Introduzca un número: "))
    num2 = int(input(f"Introduzca otro número mayor que {num}: "))
    # creamos una variable suma que comenzara por 0
    suma = 0
    for i in range(num, num2 + 1):
        # sumamos la variable a i. i es lo que realiza el bucle
        suma = suma + i
    print(f"La suma desde {num} hasta {num2} es: {suma}")
    print(f"{num} + {num + 1} + {num + 2} = {suma}")
suma()


# Ej4: Escribe un programa que pida un número y calcule su factorial.
# Dame un número: 5
# El factorial de 5 es: 120

def factorial():
    num = int(input("Introduzca un número: "))
    # factorial en 1 para que no se multiplique por 0
    factorial = 1
    # range(1, num + 1) para que el rango sea de 1 a num + 1, num + 1 porque el rango no incluye el ultimo numero
    # i es el numero que se va a multiplicar por el factorial
    for i in range(1, num + 1):
        # multiplicamos el factorial por i porque i es el numero que se va a multiplicar
        factorial = factorial * i
    print("El factorial de " + str(num) + " es: " + str(factorial))
factorial()

# Ej5: Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
# Anchura del rectángulo: 5
# Altura del rectángulo: 3
# *****
# *****
# *****

def rectangulo():
    anchura = int(input("Anchura del rectángulo: "))
    altura = int(input("Altura del rectángulo: "))
    # for para recorrer todas las filas del rectangulo
    # i es la altura del rectangulo
    for i in range(altura):
        # print asterisco multiplicado por la anchura del rectangulo
        print("*" * anchura)
rectangulo()

# # Ej6: Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# # Altura del triángulo: 4
# # *
# # **
# # ***
# # ****

def trianguloAltura():
    altura = int(input("Altura del triángulo: "))
    # i es la altura del triangulo
    for i in range(altura):
        # imprimimos asteriscos multiplicados por la altura del triangulo
        # i + 1 porque el rango no incluye el ultimo numero
        print("*" * (i + 1))
trianguloAltura()

# Ej7: Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# ****
# ***
# **
# *

def triangulo():
    altura = int(input("Altura del triángulo: "))
    # i es la altura del triangulo. altura + 1 porque el rango no incluye el ultimo numero
    for i in range(altura + 1):
        # imprimimos asteriscos multiplicados por la altura del triangulo
        # altura - i porque queremos que vaya disminuyendo
        print("*" * (altura - i))
triangulo()


# Ej8: Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
# Altura del triángulo: 4
# *
# **
# ***
# ****
# ***
# **
# *

def triangulo():
    anchura = int(input("Anchura del triángulo: "))
    # for para recorrer todas las filas del triangulo 
    # i es la altura del triangulo. Se suma 1 porque el rango no incluye el ultimo numero
    for i in range(anchura + 1):
        # print para imprimir los espacios en blanco y los asteriscos
        print("*" * (i))
    for i in range(anchura + 1):
        # anchura - i para que vaya disminuyendo la altura del triangulo
        # i es la altura del triangulo
        print("*" * (anchura - i))
triangulo()

# Ej9: Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
# Anchura del rectángulo: 5
# Altura del rectángulo: 4
# *****
# *   *
# *   *
# *****

def rectangulo():
    anchura = int(input("Anchura del rectángulo: "))
    altura = int(input("Altura del rectángulo: "))
    for i in range(altura):
        # if para imprimir la primera y la ultima fila del rectangulo
        # i es la altura del rectangulo
        # i == 0 es la primera fila. i == altura - 1 es la ultima fila
        # i == altura - 1 porque el rango no incluye el ultimo numero
        if i == 0 or i == altura - 1:
            print("*" * anchura)
        else:
            # imprimimos el asterisco y los espacios en blanco. anchura - 2 porque hay que restarle los dos asteriscos
            print("*" + " " * (anchura - 2) + "*")
rectangulo()


# Ej10: Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
# Altura de un triángulo: 5
#     *
#    ***
#   *****
#  *******
# *********

def triangulo2():
    altura = int(input("Altura del triangulo: "))
    # i es la altura del triangulo
    for i in range(altura):
        # imprimimos espacios multiplicados por la altura del triangulo
        # altura - i porque queremos que vaya disminuyendo
        # i* 2+1 porque queremos que vaya aumentando
        # i es la altura del triangulo
        print(" " * (altura - i) + "*" * (i* 2+1))
triangulo2()


# Ej11: scribe un programa que pida un número e imprima todos sus divisores.
# Dame un número: 200
# Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200

def divisores():
    num = int(input("Introduzca un numero: "))
    # Que empiece en 1 y termine en el numero introducido
    for i in range(1, num + 1):
        # Si el numero es divisible entre el numero introducido y el numero introducido es mayor que 1 
        if num % i == 0 and num > 1:
            print(i, end=" ")
divisores()


# Ej12: Escribe un programa que pida un número y escriba si primo o no
# Dame un número: 123
# El número 123 no es primo
# Dame un número:127
# El número 127 es primo

def esPrimo():
    num = int(input("Introduzca un numero: "))
    primo = True
    # Que empiece en 2 porque 1 es divisible entre todos los numeros y termine en el numero introducido
    # for para recorrer todos los numeros desde 2 hasta el numero introducido
    # i es el numero que se va a dividir entre el numero introducido
    for i in range(2, num):
        # Si el numero es divisible entre el numero introducido
        if num % i == 0:
            primo = False
    # Si el numero es primo o no
    if primo:
        print(f"El numero {num} es primo")
    else:
        print(f"El numero {num} no es primo")
esPrimo()