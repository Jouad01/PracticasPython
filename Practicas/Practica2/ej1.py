# Realizar sin bucles

# Ej1. Pida al usuario 5 números y diga cuál es el mayor y cuál el menor.

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

