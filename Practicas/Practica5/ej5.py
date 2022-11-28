# 12. Escribir un programa para jugar a adivinar un número 
# (el usuario piensa un número y el programa lo ha de adivinar). 
# El programa empieza pidiendo entre qué números está el número a adivinar y luego 
# intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa 
# es menor, mayor o igual al que se ha buscado.
# Valor mínimo: 0
# Valor máximo: 100
# Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
# Es 50 ?: mayor
# Es 75 ?: menor
# Es 62 ?: menor
# Es 56 ?: mayor
# Es 59 ?: igual
# Gracias por jugar!!
# Mejoras (opcionales):
#     • que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
#     • Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y 
#       al decir "26" le decimos "menor", el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.

import random
import time


# MI ALGORITMO:
# 1. Creamos dos variables, una minimo y otra maximo para que el usuario introduzca los numeros 
# entre los que quiere que el programa adivine.
# 2. Creamos una variable secreto para que el programa sepa que numero es.
# 3. Creamos una variable respuesta para que el usuario diga si el numero que ha dicho el programa es mayor, menor o igual
# y estará vacía hasta que el usuario introduzca una respuesta.
# 4. Creamos una variable booleano para que el bucle while se repita hasta que el usuario diga que el numero es igual.
# 5. Creamos un if para que si el numero minimo es mayor que el numero maximo, el programa vuelva a pedir los numeros.
# 6. Creamos un if para que si el numero minimo es igual que el numero maximo, el programa vuelva a pedir los numeros.
# 7. Creamos un while para que el bucle se repita hasta que el usuario diga que el numero es igual o el booleano sea falso.
# 8. Creamos un print para que el programa diga que piense un numero entre el minimo y el maximo.

def programaAdivinar():
    minimo = int(input("Valor minimo: "))
    maximo = int(input("Valor maximo: "))
    # variable secreto para que el programa sepa que numero es
    secreto = 0
    respuesta = ""
    booleano = True
    if minimo > maximo:
        print(f"{minimo} es mayor que {maximo}. Vuelve a intentarlo")
        return
    if minimo == maximo:
        print("Son numeros iguales. Vuelve a intentarlo")
        return
    while respuesta != "igual" or booleano == True:
        print(f"Piensa un numero entre {minimo} y {maximo} a ver si lo puedo adivinar.")
        secreto = random.randint(minimo, maximo)
        respuesta = input(f"Es {secreto}?: ")
        if respuesta == "mayor" or respuesta == "Mayor":
            # variable minimo se iguala a secreto + 1 para que el numero no se repita
            minimo = secreto + 1
        elif respuesta == "menor" or respuesta == "Menor":
            # variable maximo se iguala a secreto - 1 para que el numero no se repita
            maximo = secreto - 1
        elif respuesta == "igual" or respuesta == "Igual":
            print("Adivinado. Gracias por jugar!!")
            booleano = False
        # codigo rompe al introducir un numero que no sea mayor, menor o igual
        elif secreto > maximo or secreto < minimo:
            print("Estas haciendo trampas.")
            booleano = False
programaAdivinar()