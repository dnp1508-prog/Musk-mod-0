'''
Escribe un programa en Python para generar 26
archivos de texto llamados A.txt, B.txt, y así
sucesivamente hasta Z.txt.
'''

def generar_archivos():
    for letra in range(ord("A"), ord("Z") + 1):
        nombre_archivo = "{}.txt".format(chr(letra))
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Este es el archivo {}.txt".format(chr(letra)))
    print("Archivos generados exitosamente.")
generar_archivos()