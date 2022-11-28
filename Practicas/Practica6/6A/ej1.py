# 1. Escribe un programa que pida un texto por pantalla, 
# este texto lo pase como parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y 
# luego todo en mayúsculas.


frase = input("Introduce una frase: ")

# MI ALGORITMO:
# 1. Pido una frase
# 2. Creo una funcion que reciba la frase como parametro
# 3. Imprimo la frase en minusculas y en mayusculas
# 4. Llamo a la funcion con la frase como parametro

def texto(frase):
    print(frase.lower())
    print(frase.upper())
texto(frase)