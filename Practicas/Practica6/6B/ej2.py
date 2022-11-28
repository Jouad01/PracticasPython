frase = input("Introduce una frase: ")

def contarPalabras(frase):
    # Contamos la cantidad de palabras y el split lo usamos para separar las palabras
    print(len(frase.split()))
contarPalabras(frase)