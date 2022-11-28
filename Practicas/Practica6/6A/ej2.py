# 2. Escribe un programa que lea 
# (entrada por teclado) el nombre y los dos apellidos de una persona 
# (en tres cadenas de caracteres diferentes), 
# los pase como parámetros a una función, y ésta debe unirlos y 
# devolver una única cadena. La cadena final será imprimida por el programa por pantalla.

nombre = input("Introduce tu nombre: ")
apellido1 = input("Introduce tu primer apellido: ")
apellido2 = input("Introduce tu segundo apellido: ")

# MI ALGORITMO:
# 1. Pido el nombre, el primer apellido y el segundo apellido
# 2. Creo una funcion que reciba los tres parametros
# 3. Imprimo los tres parametros
# 4. Llamo a la funcion con los tres parametros

def nombreCompleto(nombre, apellido1, apellido2):
    print(nombre, apellido1, apellido2)
nombreCompleto(nombre, apellido1, apellido2)