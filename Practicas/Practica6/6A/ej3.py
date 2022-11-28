# 3. Escribe un programa que lea (entrada por teclado) una frase, y 
# la pase como parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea.

frase = input("Introduce una frase: ")

# MI ALGORITMO:
# 1. Pido una frase al usuario 
# 2. Creo una funcion que reciba la frase como parametro
# 3. Creo un bucle for que recorra la frase y que imprima cada caracter de la frase
# 4. Llamo a la funcion con la frase como parametro

def leer(frase):
    for char in frase:
        print(char)
leer(frase)