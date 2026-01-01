'''
Escriba una función en Python para leer líneas
de un archivo de texto "notas.txt". Su función
debe encontrar y mostrar la aparición de la palabra "el".
'''

def buscar_el():
    ubicacion = "notas.txt" #Ubicación del archivo
    with open(ubicacion, "r", encoding = "utf-8") as archivo: #Abrir el archivo en modo lectura
        contenido = archivo.readlines() #Leer todas las líneas del archivo
        for linea in contenido:
            if "el" in linea: #Buscar la palabra "el" en cada línea
                print(linea.strip()) #Imprimir la línea que contiene la palabra "el"
buscar_el() #Llamar a la función para ejecutar la búsqueda