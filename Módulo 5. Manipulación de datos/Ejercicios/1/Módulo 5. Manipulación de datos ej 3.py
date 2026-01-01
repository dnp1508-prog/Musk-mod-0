'''
Escribe una función en Python para contar y
mostrar el número total de palabras en un
archivo de texto.
'''
def contar_palabras_en_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        numero_de_palabras = len(palabras)
        print(numero_de_palabras)
contar_palabras_en_archivo('story.txt')