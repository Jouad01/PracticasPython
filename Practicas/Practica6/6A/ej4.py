# 4. Escribe un programa que pida una frase (entrada por teclado), y le pase 
# como parámetro a una función dicha frase. La función debe sustituir todos los espacios en 
# blanco de una frase por un asterisco, y devolver el resultado para que el programa principal la imprima por pantalla.

frase = input("Introduce una frase: ")

# MI ALGORITMO: (Dos maneras de hacerlo)
# 1. Pido una frase al usuario
# 2. Creo una funcion que reciba la frase como parametro
# 3. Creo una lista vacia
# 4. Creo un bucle for que recorra la frase 
# 5. Si el caracter es un espacio, añado un asterisco a la lista, sino añado el caracter
# 6. Imprimo la lista unida
# 7. Llamo a la funcion con la frase como parametro

def asterisco(frase):
    # print(frase.replace(" ", "*"))
    lista = []
    for i in frase:
        # si i es un espacio, se añade un asterisco a la lista sino se añade i, que es el caracter
        if i == " ":
            lista.append("*")
        else:
            lista.append(i)
    print("".join(lista))
asterisco(frase)