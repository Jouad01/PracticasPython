# 5. Desarrolla un programa, que nos sirva para gestionar nuestros contactos 
# (la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico. 
# El programa tendrá un menú, con las siguientes opciones: añadir contacto, 
# consultar contacto a partir de la clave, consultar todos los contactos y eliminar contacto. 
# Aprovecha lo que has aprendido hasta el momento (diccionarios, funciones, procedimientos…)

def menu():
    print("------Agenda------")
    print("1. Añadir contacto")
    print("2. Consultar clave contacto")
    print("3. Consultar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Elige el número de una de las 4 opciones: ")
    if opcion == "1":
        añadirContacto()
    elif opcion == "2":
        consultarClave()
    elif opcion == "3":
        consultarContactos()
    elif opcion == "4":
        eliminarContactos()
    elif opcion == "5":
        print("Hasta pronto")
    else:
        print("Opción incorrecta")
        menu()

def añadirContacto():
    nombre = input("Introduce tu nombre: ")
    apellido1 = input("Introduce tu primer apellido: ")
    apellido2 = input("Introduce tu segundo apellido: ")
    telefono = int(input("Introduce tu teléfono móvil: "))
    correo = input("Introduce tu correo electrónico: ")
    # nombre[0] es la primera letra del nombre
    # apellido1[0] es la primera letra del primer apellido
    # apellido2[0] es la primera letra del segundo apellido
    clave = nombre[0] + apellido1[0] + apellido2[0]
    # Creo un diccionario con los datos del contacto
    contacto = {
        "nombre": nombre,
        "apellido1": apellido1,
        "apellido2": apellido2,
        "telefono": telefono,
        "correo": correo
    }
    # La clave es el nombre de la persona. La diferencia entre 
    # contactos y contacto es que contactos es un diccionario para almacenar y contacto es un diccionario dentro de otro diccionario
    contactos[clave] = contacto
    print("Contacto añadido correctamente")
    menu()

def consultarClave():
    clave = input("Introduce la clave del contacto: ")
    # Si la clave está en el diccionario de contactos imprime el diccionario que está dentro del diccionario de contactos
    if clave in contactos:
        print(contactos[clave])
    else:
        print("Clave no encontrada")
    menu()

def consultarContactos():
    print(contactos)
    menu()

def eliminarContactos():
    borrar = input("Introduce la clave del contacto: ")
    if borrar in contactos:
        # contactos[borrar] significa que borro el diccionario que está dentro del diccionario de contactos
        del contactos[borrar]
        print("Contacto eliminado correctamente")
    else:
        print("Contacto no encontrado")
    menu()
# Creamos un diccionario vacío que contendrá los contactos, es al final del programa porque 
# si lo ponemos al principio, se borra al ejecutar la función
contactos = {}
menu()

