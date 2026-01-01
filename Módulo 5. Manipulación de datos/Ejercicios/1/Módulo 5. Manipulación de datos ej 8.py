'''
Escribe un programa en python para añadir
texto a un archivo y mostrar el texto en
python.txt
'''

def añadir_texto(texto):
    ubicacion = 'python.txt'
    with open(ubicacion, "a", encoding="utf-8") as archivo:
        archivo.write("{}".format(texto))
    print("Texto añadido correctamente.")
def mostrar_texto():
    ubicacion = 'python.txt'
    with open(ubicacion, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("{}".format(contenido))
texto = input("Escribe el texto que deseas añadir al archivo: ")
añadir_texto(texto)
mostrar_texto()