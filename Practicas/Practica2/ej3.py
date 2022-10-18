# Ej3. Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, 
# y pida los datos según que caso y muestre el resultado.

# MI ALGORITMO
# 1. Creamos la funcion
# 2. Creamos varios print para preguntar al usuario. El último un input que pregunatará que area quiere crear
# 3. Si el usuario introduce triangulo se le pregunatará por la base y altura que tiene que calcular y se le dará el resultado
#   3.1 Si en cambio elige cuadrado sigue la misma estructura, preguntará por la base y altura y se le dará el resultado en un print
# 4. Llamamos a la funcion

def calcularArea():
    print("Calcular areas")
    print("Elija cual area quiere calcular: ")
    print("- Cuadrado ")
    print("- Triangulo")
    area = input("Introduzca Cuadrado si quiere calcular un cuadrado o Triangulo si quiere calcular un triangulo: ")
    if area == "Triangulo" or area == "triangulo":
        base = float(input("Introduzca la base: "))
        altura = float(input("Introduzca la altura: "))
        print(f"El area del triangulo es {base * altura/2}")
    elif area == "Cuadrado" or area == "cuadrado":
        base = float(input("Introduzca la base: "))
        altura = float(input("Introduzca la altura: "))
        print(f"El area del cuadrado es {base*altura}")
calcularArea()