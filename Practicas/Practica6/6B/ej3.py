# 3. Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while, 
# por tanto, habrá dos funciones que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks),
# o de otra (con while). Ambas funciones devolverán true (si es primo) o false (si no es primo). 
# El programa principal informará del resultado. Además, como mejora puedes calcular el tiempo que tarda 
# en encontrar la solución de una manera u otra. Comentario: aprovecha el código que tienes ya creado


import time

bucle = input("¿Quieres calcular si un número es primo con for o con while? ")

def primos(bucle):
    num = int(input("Introduce un número: "))
    def primo_for(num):
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
        if primo:
            print(f"El numero {num} es primo")
        else:
            print(f"El numero {num} no es primo")
    def primo_while(num):
        primo = True
        i = 2
        while i < num:
            if num % i == 0:
                primo = False
            # Añadiendo 1 a i, se evita que se repita el bucle
            i = i + 1 
        if primo:
            print(f"El numero {num} es primo")
        else:
            print(f"El numero {num} no es primo")
    if bucle == "for" or bucle == "For":
        espera = time.time()
        primo_for(num)
        espera = time.time() - espera
        print(f"El tiempo de espera es de {espera} segundos")
    elif bucle == "while" or bucle == "While":
        espera = time.time()
        primo_while(num)
        espera = time.time() - espera
        print(f"El tiempo de espera es de {espera} segundos")
    else:
        print("No has introducido un valor correcto")
primos(bucle)

