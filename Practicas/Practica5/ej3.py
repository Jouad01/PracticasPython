# 10. Escribe un programa que te pida los nombres y notas de alumnos. 
# Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. 
# Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. 
# Nota: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], 
# [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]
# Dame un nombre: Héctor Quiroga
# Escribe una nota: 4
# Escribe otra nota: 8.5
# Escribe otra nota: 12
# Dame otro nombre: Inés Valls
# Escribe una nota: 7.5
# Escribe otra nota: 1
# Escribe otra nota: 2
# Escribe otra nota: -5
# Dame otro nombre:
# Las notas de los alumnos son:
# Héctor Quiroga: 4.0 - 8.5
# Inés Valls: 7.5 - 1.0 - 2.0


# MI ALGORTIMO:
# 1. Creamos el nombre de la funcion y dos variables. Una lista vacia y una variable para el print.
# 2. Creamos un bucle while True para que se repita 
# 3. Pedimos el nombre del alumno con una variable nombre.
# 4. Si el nombre es igual a "", se sale del bucle, ya que no habrá puesto ningun nombre.
# 5. Si el nombre es diferente a "", se añade a la lista el nombre del alumno.
# 6. Creamos otro bucle while True para que se repita 
# 7. Pedimos la nota del alumno con una variable nota.
# 8. Si la nota es menor a 0 o mayor a 10 o no es un numero, se sale del bucle
# 9. Si la nota es mayor a 0 y menor a 10, se añade a la lista la nota del alumno.
# 10. Recorremos la lista con un bucle for para que imprima el nombre y las notas por sus posiciones
# 11. Imprimimos el nombre y las notas del alumno


def notasAlumnos():
    lista = []
    imprime = ""
    booleano = True
    while True and booleano == True:
        nombre = input("Dame un nombre: ")
        if nombre == "":
            booleano = False
        else:
            lista.append([nombre])
            while True:
                nota = float(input("Escribe una nota: "))
                # si la nota es menor a 0 o mayor a 10 o no es un numero, se sale del bucle
                if nota < 0 or nota > 10 or nota == "":
                    # Con el booleano False, se sale del bucle while True y no es lo que queremos
                    break
                else:
                    # añadimos a la lista el nombre y la nota. [-1] es para que añada a la ultima lista creada
                    lista[-1].append(nota)
    # recorremos la lista con un bucle for para que imprima el nombre y las notas por sus posiciones
    for i in lista:
        imprime = i[0] + ": "
        for j in i[1:]:
            imprime += str(j) + " - "
        print(imprime)
notasAlumnos()
