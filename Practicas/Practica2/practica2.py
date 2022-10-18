# Ejercicios para realizar sin bucles

# Ej1. Pida al usuario 5 números y diga cuál es el mayor y cuál el menor.

# MI ALGORTIMO:
# 1. Creamos la funcion con un return que pedira un numero
# 2. Creamos una lista en la que metemos 5 veces el nombre de la funcion. Las mismas veces que numeros vamos a pedir
# 3. Usamos el metodo sort() que ordenará de menor a mayor los numeros introducidos por el usuario
# 4. Utilizamos dos print que imprimiran el numero mayor y menor
# 5. Dentro de los print, se imprimira el primero que será el menor [0] y [-1] que será el ultimo y por lo tanto el mayor.

def preguntarNumero():
    return int(input("Introduzca un numero: "))

lista = [preguntarNumero(), preguntarNumero(), preguntarNumero(), preguntarNumero(), preguntarNumero()]
lista.sort()

print("El número más alto es " + str(lista[-1]))
print("El número más pequeño es " + str(lista[0]))


# Ej2. Pida al usuario 5 números y diga si estos estaban en orden decreciente, 	creciente o desordenados.

# MI ALGORTIMO:
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


# Ej3. Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.

# MI ALGORITMO
# 1. Creamos la funcion
# 2. Creamos varios print para preguntar al usuario. El último un input que pregunatará que area quiere crear
# 3. Si el usuario introduce triangulo se le pregunatará por la base y altura que tiene que calcular y se le dará el resultado
#   3.1 Si en cambio elige cuadrado sigue la misma estructura, preguntará por la base y altura y se le dará el resultado en un print
# 4. Llamamos a la funcion

def calcularArea():
    print("Calcular areas")
    print("Elija cual area quiere calcular: ")
    print("- Cuadrado ")
    print("- Triangulo")
    area = input("Introduzca Cuadrado si quiere calcular un cuadrado o Triangulo si quiere calcular un triangulo: ")
    if area == "Triangulo" or area == "triangulo":
        base = float(input("Introduzca la base: "))
        altura = float(input("Introduzca la altura: "))
        print(f"El area del triangulo es {base * altura/2}")
    elif area == "Cuadrado" or area == "cuadrado":
        base = float(input("Introduzca la base: "))
        altura = float(input("Introduzca la altura: "))
        print(f"El area del cuadrado es {base*altura}")
calcularArea()
    
# Ej4. Pida al usuario tres números y un cuarto número, y compruebe si este último es divisor de los tres números primos

# MI ALGORTIMO:
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


# Ej5. Pida al usuario un importe en euros y diga si el cajero automático le puede dar dicho importe 
# utilizando el mismo billete y el más grande (recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5€).
    # Por ejemplo: 
    # 25 euros → “el cajero te devuelve 5 billetes de 5 euros”
    # 20 euros → “el cajero te devuelve 1 billete de 20 euros”
    # 130 euros → “el cajero te devuelve 13 billetes de 10 euros”

# MI ALGORTIMO:
# 1. Creamos la variable donde preguntará el importe al usuario, fuera de la funcion para que no lo repita cada vez que termina
# 2. Creamos una array que contendrá los billetes que existen
# 3. Creamos la funcion y dentro llevara billete
# 4. Creamos un if que comprobará si el numero introducido es un billete
#   4.1 Si lo es, imprimira el resultado con su cantidad correspondiente de billetes y con 'quit()' termina el programa
# 5. Creamos una lista llamada 'totalbilletes' 
# 6. La lista estará dentro de un 'map'. Donde la primera condicion, que es la funcion, ejecutara la segunda condicion que son los
#  'billetesDisponibles'
# 7. Finalmente, si introducimos un numero incorrecto, por ejemplo 24, nos lo comunicará en un print

precio = int(input("¿Cuanto dinero quiere sacar? "))
billetesDisponibles = [500, 200, 100, 50, 20, 10, 5]
def calcularBilletes(billete):
    if precio % billete == 0:
        print(f"El cajero te devuelve {int(precio / billete)} billetes de {billete}€")
        quit()
totalBilletes = map(calcularBilletes, billetesDisponibles)
list(totalBilletes)
print("Introduzca la cantidad correcta. Vuelva a intentarlo")
