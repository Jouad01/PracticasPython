# Ej5. Pida al usuario un importe en euros y diga si el cajero automático le puede dar dicho importe 
# utilizando el mismo billete y el más grande (recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5€).
    # Por ejemplo: 
    # 25 euros → “el cajero te devuelve 5 billetes de 5 euros”
    # 20 euros → “el cajero te devuelve 1 billete de 20 euros”
    # 130 euros → “el cajero te devuelve 13 billetes de 10 euros”


# 1. Creamos la variable donde preguntará el importe al usuario, fuera de la funcion para que no lo repita cada vez que termina
# 2. Creamos una array que contendrá los billetes que existen
# 3. Creamos la funcion y dentro llevara billete
# 4. Creamos un if que comprobará si el numero introducido es un billete
#   4.1 Si lo es, imprimira el resultado con su cantidad correspondiente de billetes y con 'quit()' termina el programa
# 5. Creamos una lista llamada 'totalbilletes' 
# 6. La lista estará dentro de un 'map'. Donde la primera condicion, que es la funcion, ejecutara la segunda condicion que son los
#  'billetesDisponibles'
# 7. Finalmente, si introducimos un numero incorrecto, por ejemplo 13, nos lo comunicará en un print

precio = int(input("¿Cuánto dinero quiere sacar? "))
billetesDisponibles = [500, 200, 100, 50, 20, 10, 5]
def calcularBilletes(billete):
    if precio % billete == 0:
        print(f"El cajero te devuelve {int(precio / billete)} billetes de {billete}€")
        quit()
totalBilletes = map(calcularBilletes, billetesDisponibles)
list(totalBilletes)
print("Introduzca la cantidad correcta. Vuelva a intentarlo")