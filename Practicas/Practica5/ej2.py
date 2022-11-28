# 9.Escribe un programa que te pida nombres de personas y sus números de teléfono. 
# Para terminar debe pulsar “S” cuando te pida el nombre. 
# El programa termina escribiendo nombres y números de teléfono. 
# Nota: La lista en la que se guardan los nombres y números de teléfono 
# tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.
# Dame un nombre: Pepe González
# Dame el teléfono: 971971971
# Dame un nombre: Macarena Gómez
# Dame el teléfono: 971999999
# Dame un nombre: Pascual Ribot
# Dame el teléfono: 666555444
# Dame un nombre: S
# Los nombres y teléfonos de la agenda son:
# Pepe González: 971971971
# Los nombres y teléfonos de la agenda son:
# Macarena Gómez: 971999999
# Los nombres y teléfonos de la agenda son:
# Pasqual Ribot: 666555444

def agenda():
    # creamos una lista vacia y una variable para el print
    lista = []
    imprime = ""
    booleano = True
    while True and booleano == True:
        # mientras no se pulse S, pedimos nombre y telefono
        nombre = input("Dame un nombre: ")
        if nombre == "S" or nombre == "s":
            booleano = False
        else:
            telefono = input("Dame el telefono: ")
            # añadimos a la lista el nombre y el telefono
            lista.append([nombre, telefono])
    # recorremos la lista y añadimos a la variable imprime el nombre y el telefono
    for i in lista:
        # se imprime el nombre y telefono de esta manera. i[0] es el nombre, significa que es la primera posicion de la lista
        # i[1] es el telefono, significa que es la segunda posicion de la lista
        imprime = imprime + str(i[0]) + ": " + str(i[1]) + "\n"
    print("Los nombres y telefonos de la agenda son: \n" + imprime)
agenda()
