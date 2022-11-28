
frase = input("Introduce una frase: ")

def palindromo(frase):
    # Eliminamos los espacios en blanco porque sino nos daría error ya que tiene que ser una frase sin espacios
    frase = frase.replace(" ", "")
    # Si frase es igual a frase con el orden inverso, es palindromo
    if frase == frase[::-1]:
        print("Es palindromo")
    else: 
        print("No es palindromo")
palindromo(frase)