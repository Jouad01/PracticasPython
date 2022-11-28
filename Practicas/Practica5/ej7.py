# 14. Desarrolla un programa que tenga las siguientes características:
# Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
# Dicho problema resuélvelo con bucles for y while. 
# Justifica en el propio programa porque una opción es adecuada y la otra no.
# ¿Crees que si medimos el tiempo de ejecución de ambas soluciones 
# demostrará que efectivamente una solución es más eficiente? Investiga para comprobarlo.

# Programa para adivinar el cumpleaños de una persona.
# El programa lanza dos prints, uno para indicar al usuario lo que tiene que hacer, otro para la pista.
# Se crea una variable para almacenar el número de intentos que lleva el usuario y otra que pide el cumpleaños.	
# Se crea un bucle while para que el usuario pueda introducir el cumpleaños hasta 10 veces dentro de un for.
# Si el usuario introduce el cumpleaños correcto se sale del bucle.
# Si el usuario pasa de 10 intentos, se le indica que ha perdido.
# Salimos del bucle si se cumple una de las dos condiciones y preguntamos si quiere volver a jugar.
# Si el usuario quiere volver a jugar, se llama a la función cumpleaños() y se repite el proceso.
# Si el usuario no quiere volver a jugar, se le indica que hasta la próxima.

# Respondiendo a la pregunta, no creo que un tiempo de ejecución demuestre que una solución es más eficiente en este caso,
# ya que la respuesta solo puede ser una y el usuario debe introducir los datos que pide el print de manera correcta e instantánea.
# Aunque si se podria hacer con un import time y time.sleep() para que el usuario tenga tiempo de pensar la respuesta o import random.

def cumpleaños():
    print("Adivina mi cumpleaños con 10 intentos. Tienes una pista.")
    print("La pista es que el año es en 2001, el día 10.")
    respuesta = input("Formato dd/mm/aaaa. ¿Cuál es mi cumpleaños?: ")
    cumple = "10/07/2001"
    intentos = 0
    while respuesta != cumple and intentos < 10:
        # Creamos un bucle para que el usuario pueda introducir el cumpleaños hasta 10 veces.
        for intentos in range(10):
            # intentos = intentos + 1 para que el contador de intentos vaya aumentando.
            intentos += 1
            respuesta = input("No es mi cumpleaños. Inténtalo de nuevo: ")
            # Si el usuario introduce el cumpleaños correcto se sale del bucle.
            if respuesta == cumple:
                print("¡Felicidades! ¡Lo has adivinado!")
                break
            # Si el usuario pasa de 10 intentos, se le indica que ha perdido.
            elif intentos == 10:
                print("Lo siento. Has agotado los 10 intentos.")
                break
    # Salimos del bucle si se cumple una de las dos condiciones y preguntamos si quiere volver a jugar
    respuesta = input("¿Quieres volver a jugar? (Si/No): ")
    if respuesta == "Si":
        cumpleaños()
    else:
        print("¡Hasta la próxima!")
cumpleaños()