# 11.Escribir un programa para jugar a adivinar un número 
# (el ordenador "piensa" el número y el usuario lo ha de adivinar). 
# El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y 
# luego el usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños. pista:
# import random
# import time

# minimo = int (input ( "Valor mínimo:"))
# max = int (input ( "Valor máximo:"))
# secreto = random.randint (mínimo, máximo)
# Valor mínimo: 0
# Valor máximo: 100
# A ver si adivinas un número entero entre 0 y 100.
# Escribe un número: 20
# Demasiado pequeño! Volver a probar: 30
# Demasiado grande! Volver a probar: 27
# Correcto! Lo has intentado 3 veces.


# MI ALGORITMO:
# 1. Importamos random que nos ayudara a generar un numero aleatorio.
# 2. Creamos la funcion programa que nos pedira el numero minimo y maximo con dos variables.
# 3. Creamos una variable secreto que sera el numero aleatorio entre el minimo y el maximo. Otra variable booleano que sera True.
# 4. Creamos un bucle while True para que se repita.
# 5. Creamos una variable intentos para contar los intentos.
# 6. Creamos una variable numero que sera el numero que introduzca el usuario.
# 7. Si el numero es igual al secreto se imprime el mensaje y se rompe el bucle.
# 8. Si es mayor o menor imprime un mensaje.
# 9. Se llama a la funcion programa.


import random 

def programa():
    minimo = int(input("Valor mínimo: "))
    maximo = int(input("Valor máximo: "))
    secreto = random.randint(minimo, maximo)
    booleano = True
    print(f"A ver si adivinas un numero entero entre {minimo} y {maximo}")
    # Se crea variable intentos para contar el numero de intentos
    intentos = 0
    # mientras sea true se ejecuta el bucle
    while True and booleano == True:
        # Variable intentos para contar los intentos. intentos + 1 para que empiece en 1
        intentos = intentos + 1
        numero = int(input("Escribe un número: "))
        # Si el numero es igual al secreto se imprime el mensaje y se rompe el bucle. 
        # Si es mayor o menor imprime un mensaje
        if numero == secreto:
            print(f"Correcto! Lo has intentado {intentos} veces.")
            booleano = False
        elif numero > secreto:
            print("Demasiado grande! Vuelve a probar: ")
        else:
            print("Demasiado pequeño! Vuelve a probar: ")
programa()