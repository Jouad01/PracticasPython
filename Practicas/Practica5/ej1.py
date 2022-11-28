# 8. Escribe un programa que te pida primero un número y luego te pida números hasta 
# que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.
# Escribe límite: 50
# Escribe un valor: 10
# Escribe otro valor: 45
# 45 es demasiado grande. Escribe otro valor: 1
# Escribe otro valor: 39
# El límite a alcanzar es 50. La lista creada es: 10, 1, 39

def limiteSuma():
    suma = 0
    imprime = ""
    lista = []
    limite = int(input("Escribe un limite: "))
    # mientras la suma sea menor que el limite
    while suma < limite:
        # pedimos un valor
        valor = int(input("Escribe un valor: "))
        # si la suma mas el valor es mayor que el limite vuelve a pedir el valor
        if valor + suma > limite:
            print(int(input(f"{valor} es demasiado grande. Escribe otro valor: ")))
        # si no, suma el valor a la suma y lo añade a la lista
        else:
            lista.append(valor)
            suma = suma + valor
    for i in lista:
        imprime = imprime + str(i) + ", "
    print(f"El limite a alcanzar es {limite}. La lista creada es: {imprime[:-2]}")
limiteSuma()