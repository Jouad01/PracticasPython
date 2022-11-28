# 13. Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while. 
# Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.

# De esta forma, el bucle while se repite hasta que el usuario escriba 0.
# Si el numero es par, no es primo. Si es impar, es primo.
# El bucle while es mejor porque se repite hasta que el usuario escriba 0, además es más sencillo de entender y no requiere 
# de tantas lineas de codigo como el bucle for.

def primos():
    num = int(input("Escribe un numero para saber si es primo o no: "))
    # Si el numero no es 0, se repite el bucle
    while num != 0:
        if num % 2 == 0:
            print(f"{num} no es primo")
        else:
            print(f"{num} es primo")
        num = int(input("Escribe otro numero para saber si es primo o no: "))
primos()