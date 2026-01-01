'''
Escribe un programa en python para calcular la
frecuencia de todas las palabras de un archivo txt.
'''

def calcular_frecuencia_palabras(nombre_archivo):
    frecuencia_palabras = {}
    ubicacion = "{}.txt".format(nombre_archivo)
    with open(ubicacion, "r", encoding = "utf-8") as archivo:
        contenido = archivo.read()
        palabra = contenido.split()
        for i in palabra:
            if i in frecuencia_palabras:
                frecuencia_palabras[i] += 1
            else:
                frecuencia_palabras[i] = 1
    return frecuencia_palabras
nombre_archivo = input("Ingresa el nombre del archivo (sin .txt): ")
resultado = calcular_frecuencia_palabras(nombre_archivo)
print("Frecuencia de palabras en el archivo: {}".format(resultado))