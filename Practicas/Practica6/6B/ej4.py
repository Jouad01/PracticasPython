# 4. Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento, 
# que recibe como parámetro la fecha en números y devuelve la fecha  con el nombre del mes. 
# Comentario: no es necesario validar si la es correcta, damos por hecho que lo será. 
# Ejemplo: 12/11/2019 -> 12 de noviembre de 2019

meses = { 
        "01": "enero",
        "02": "febrero",
        "03": "marzo",
        "04": "abril",
        "05": "mayo",
        "06": "junio",
        "07": "julio",
        "08": "agosto",
        "09": "septiembre",
        "10": "octubre",
        "11": "noviembre",
        "12": "diciembre" 
        }


fecha = input("Introduce una fecha en formato dd/mm/aa: ")
# Separa la fecha en 3 partes para poder acceder a cada una de ellas
fecha = fecha.split("/")
def dicc(meses, fecha):
        # fecha[1] es el mes porque la fecha está dividida en 3 partes (dia, mes, año)
        # fecha[0] es el dia
        # fecha[2] es el año
        if fecha[1] in meses:
                print(f"Tu fecha es el {fecha[0]} de {meses[fecha[1]]} del {fecha[2]}")
        else:
                print("El mes introducido no es correcto")
dicc(meses, fecha)