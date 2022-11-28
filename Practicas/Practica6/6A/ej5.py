# 5. Escribe un programa que te pida una frase y una vocal 
# (entrada por teclado), y pase estos datos como parámetro a una función que se 
# encargará de cambiar todas las vocales de la frase por la vocal seleccionada. 
# Devolverá la función la frase modificada, y el programa principal la imprimirá:

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

# MI ALGORITMO:
# 1. Pido una frase y una vocal al usuario
# 2. Creo una funcion que reciba la frase y la vocal como parametros
# 3. Creo un bucle for que recorra la frase
# 4. Si el caracter es una vocal, se reemplaza por la vocal que el usuario introduzca
# 5. Imprimo la frase
# 6. Llamo a la funcion con la frase y la vocal como parametros

def cambiarFrase(frase, vocal):
    for char in frase:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            # replace es un metodo que reemplaza un caracter por otro, en este caso 
            # la vocal por la que el usuario introduzca
            # char aqui es la vocal que se va a reemplazar
            frase = frase.replace(char, vocal)
    print(frase)
cambiarFrase(frase, vocal)

