'''
Escribe una función en python para leer el
contenido de un archivo de texto "poema.txt"
línea por línea y mostrar el mismo en pantalla.
'''

def leer_poema():
    with open("poema.txt", "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            print(linea.strip())

leer_poema()