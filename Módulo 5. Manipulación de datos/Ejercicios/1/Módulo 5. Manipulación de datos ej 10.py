'''
Escribe un programa en python para comprobar
si un archivo especificado existe.
'''

def archivo_existe(nombre_archivo):
    ubicacion = "{}".format(nombre_archivo)
    try:
        with open(ubicacion, "r", encoding = "utf-8") as archivo:
            return True
    except FileNotFoundError:
        return False
nombre_archivo = input("Introduce el nombre del archivo (con su extensión): ")
if archivo_existe(nombre_archivo) == True:
    print("El archivo existe.")
else:
    print("El archivo no existe.")