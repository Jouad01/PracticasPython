# EJERCICIO 1:

# Escribe un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación, debe mostrar todas las notas,  la nota media, la nota más alta que 
# ha sacado así como también la menor nota que ha sacado (5 puntos). 

# Análisis del algoritmo:
# Leer 5 notas ( será válido que sean >=0 y <=1 0). Guardo las notas en un vector.
# Recorrer de nuevo el vector para acumular las notas, calcular la nota máxima y la nota mínima. Finalmente calcular la media 
# Finalmente muestro los valores.

# Datos de entrada: 5 notas.

# Información de salida: Las notas, la nota media, nota máxima y nota mínima. 
# Variables: notas(vector de 10 enteros), tam_notas,índice (entero), nota_media (real), suma,nota_max (real), ,nota_min  (entero).

# MI ALGORTIMO:
# 1. Creamos la funcion y después una variable en la que el usuario introducirá las notas.
# 2. Creamos un while en el que mientras el numero sea mayor a 10 o menor a 0 tendra que repetirlo, y con return al final
# 3. Creamos una array en el que preguntara 5 veces por una nota y la ordenamos de menor a mayor con 'sort()'
# 4. Creamos una variable media para la lista, 'mean()' nos hará la media y se importará automaticamente
# 5. Finalmente los print, en el que (lista[-1]) sera para la posicion mas alta y 0 mas baja. Ademas de la media. 
# El join junto al map servira para darnos todas las notas sin '[]'

from statistics import mean


def notasAlumno():
    nota = int(input("Introduzca una nota: "))
    while nota > 10 or nota < 0:
        nota = int(input("Vuelva a introducir una nota. Debe ser entre 0 y 10: "))
    return nota
lista = [notasAlumno(), notasAlumno(), notasAlumno(), notasAlumno(), notasAlumno()]
lista.sort()    
media = mean(lista)
print("Sus notas son " + ', '.join(map(str, lista)))
print("Su nota más alta es " + str(lista[-1]))
print("Su nota más baja es " + str(lista[0]))
print("La media de sus notas es de " + str(media))


# EJERCICIO 2:

# Escribe un programa que pida un número al usuario y escriba si primo o no (5 puntos). Ejemplo de salida por pantalla:
# Dame un número: 123
# El número 123 no es primo
# Dame un número:127
# El número 127 es primo
# Pista:
# En matemáticas, un número primo es un número natural mayor que 1 que 
# tiene únicamente dos divisores positivos distintos: él mismo y el 1.​ (Operador MOD o %).


# MI ALGORTIMO:
# 1. Creamos la funcion junto a la variable que pedira un número al usuario
# 2. Creamos un if donde si el numero introducido es mayor a 1 entra en un bucle for
# 3. El bucle for calculará para cada numero mayor divisible entre 2 dentro del rango
#   3.1 Si el numero es divisor e igual a cero no será primo y hará un break
#   3.2 Sino, si será primo
# 4. Terminamos con un else por si el numero no es ninguna de las dos. Y se llama a la función

def pedirNumero():
    num = int(input("Introduce un número: "))
    if num > 1:
        for i in range(2, num // 2):
            if(num % i) == 0:
                print("El numero no es primo")
                break
        else:
            print("El numero es primo")
    else:
        print(f"{num} no es ninguna de las dos")
pedirNumero()