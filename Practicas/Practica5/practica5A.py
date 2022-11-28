# 1. Escribe un programa que te pida palabras y las guarde en una lista. 
# Para terminar de introducir palabras, simplemente pulsa Enter. 
# El programa termina escribiendo la lista de palabras.
# Escribe una palabra: viaje
# Escribe más palabras: aventura
# Escribe más palabras: cómic
# Escribe más palabras:
# Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']

def pedirPalabras():
    # array vacia donde se añadiran las palabras
    palabras = []
    # input que pedirá palabras
    palabra = input("Escribeme palabras: ")
    # mientras palabra sea diferente a un espacio vacio, seguimos agregando palabras sino imprime las palabras totales
    while palabra != "":
        palabras.append(palabra)
        palabra = input("Escribeme más palabras: ")
    print("Las palabras que has Escrito son", palabras)
pedirPalabras()


# 2. Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir números, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.
# Escribe un numero: 14
# Escribe otro numero: 123
# Escribe otro numero: -25
# Escribe otro numero: 123
# Escribe otro numero: Salir
# Los números que has escrito son [14, 123, -25, 123]

def pedirNumeros():
    numeros = []
    numero = input("Escribeme un numero: ")
    # mientras no sea igual a salir, seguimos añadiendo numeros
    while not (numero == "Salir" or numero == "salir"):
        # añadimos el numero a la lista y el int es para convertirlo a entero
        numeros.append(int(numero))
        numero = input("Escribeme otro numero: ")
        # imprimimos el resultado y end "" evitar las comillas
    print(f"Los números que has escrito son {numeros}", end=" ")
pedirNumeros()


# 3. Escribe un programa que pida notas y los guarde en una lista. 
# Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
# Escribe una nota: 7.5
# Escribe una nota: 0
# Escribe una nota: 10
# Escribe una nota: -1
# Las notas que has Escrito son [7.5, 0.0, 10.0]

def pedirNota():
    nota = []
    notas = float(input("Escribeme una nota: "))
    # mietras notas sea mayor o igual a 0 y menor o igual a 10, seguimos añadiendo notas
    while notas >= 0 and notas <= 10:
        nota.append(notas)
        notas = float(input("Escribeme otra nota: "))
    print(f"Las notas que has escrito son {nota}")
pedirNota()

# 4. Escribe un programa que te pida dos números, 
# de manera que el segundo sea mayor que el primero. El programa termina escribiendo los dos números tal y como se pide:
# Escribe un número: 6
# Escribe un número mayor que 6: 6
# 6 no es mayor que 6. Vuelve a introducir un número: 1
# 1 no es mayor que 6. Vuelve a introducir un número: 8
# Los números que has escrito son 6 y 8

def numMayor():
    num = int(input("Escribe un número: "))
    num2 = int(input("Escribe un número mayor que el anterior: "))
    # mientras num2 sea menor o igual a num, seguimos pidiendo numeros
    while num2 <= num:
        # si no es mayor, seguimos pidiendo numeros
        num2 = int(input(f"{num2} no es mayor que {num}. Vuelve a introducir un número: "))
    print(f"Los números que has escrito son {num} y {num2}")
numMayor()

# 5. Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. 
# Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. 
# El programa termina escribiendo la lista de números:
# Escribe un número: 6
# Escribe un número mayor que 6: 10
# Escribe un número mayor que 10: 12
# Escribe un número mayor que 12: 25
# Escribe un número mayor que 25: 9
# Los números que has escrito son: 6, 10, 12, 25  (Comentario si os fijáis ya no se imprime la lista tal cual, 
# hay que imprimir uno por uno los valores de la lista, haced esto así a partir de ahora)

def pedirNumGrandes():
    numeros = []
    imprime = ""
    num = int(input("Escribe un número: "))
    numeros.append(str(num))
    num2 = int(input(f"Escribe un número mayor que el {str(num)}: "))
    numeros.append(str(num2))
    # mientras num2 sea mayor que num, seguimos pidiendo numeros y añadiendolos a la lista
    while num2 > num:
        # num toma el valor de num2
        num = num2 
        num2 = int(input(f"Escribe un número mayor que el {str(num)}: "))
        numeros.append(str(num2))
    # pop elimina el ultimo elemento de la lista
    numeros.pop()
    for i in numeros:
        imprime += i + ", "
    print(f"Los números que has escrito son: {imprime[:-2]}")
pedirNumGrandes()

# 6. Escribe un programa que pida primero dos números (máximo y mínimo) y 
# que después te pida números intermedios. Para terminar de escribir números, 
# escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.
# Escribe un número: 6
# Escribe un número mayor que 6: 4
# 4 no es mayor que 6. Vuelve a probar: 50
# Escribe un número entre 6 y 50: 45
# Escribe otro número entre 6 y 50: 13

def numerosMxMn():
    num = int(input("Escribe un número: "))
    num2 = int(input("Escribe un número mayor que el anterior: "))
    # mientras num2 sea menor o igual a num, seguimos pidiendo numeros
    while num > num2:
        num2 = int(input(f"{num2} no es mayor que {num}. Vuelve a introducir un número: "))
        # num3 and num4 son los numeros intermedios
        num3 = int(input(f"Escribe un número entre {num} y {num2}: "))
        num4 = int(input(f"Escribe otro número entre {num} y {num2}: "))
        # mientras num3 sea menor que num y num3 sea mayor que num2, seguimos pidiendo numeros
        while num3 < num and num3 > num2:
            num3 = int(input(f"{num3} no es mayor que {num} y no es menor que {num2}. Vuelve a probar: "))
        # mientras num4 sea menor que num y num4 sea mayor que num2, seguimos pidiendo numeros
        while num4 < num and num4 > num2:
            num4 = int(input(f"{num4} no es mayor que {num} y no es menor que {num2}. Vuelve a probar: "))
    # imprimimos los numeros una vez que se cumplan las condiciones
    print(f"Los números que has escrito son {num}, {num2}, {num3} y {num4}")
numerosMxMn()


# 7. Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma 
# de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.
# Escribe límite: 50
# Escribe un valor: 10
# Escribe otro valor: 25
# Escribe otro valor: 7
# Escribe otro valor: 14
# El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56

def numLimite():
    num = int(input("Escribe un límite: "))
    num2 = int(input("Escribe un valor: "))
    imprime = ""
    # creamos una variable para guardar la suma de los numeros y una lista vacia para guardar los numeros
    suma = 0
    lista = []
    # mientras la suma sea menor que el numero, seguimos pidiendo numeros
    while suma < num:
        # añadimos el numero a la lista
        lista.append(int(num2))
        # sumamos el numero a la suma
        suma = suma + num2
        num2 = int(input("Escribe otro valor: "))
    # recorremos la lista para imprimir los numeros y convertimos la lista en string
    for i in lista:
        imprime = imprime + str(i) + ", "
    print(f"El límite a superar es {num}. La lista creada es {imprime[:-2]} ya que la suma de estos números es: {suma}")
numLimite()


