'''
Escriba una función display_words() en python
para leer las lineas de un archivo de texto
"story.txt", y mostrar aquellas palabras que
tengan menos de 4 caracteres.
'''

def display_words():
    ubicacion = "story.txt"
    with open(ubicacion, "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            palabras = linea.split()
            for palabra in palabras:
                if len(palabra) < 4:
                    print(palabra)
display_words()