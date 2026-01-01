'''
Un archivo de texto llamado "materia.txt"
contiene algún texto, que necesita ser mostrado
de manera que cada carácter siguiente esté separado
por un símbolo "#". Escriba una definición de función
para hash_display() en 
Python que muestre todo el contenido del
archivo "materia.txt" en el formato deseado.
'''

def hash_display():
    ubicacion = "Materia.txt"
    with open(ubicacion, "r", encoding = "utf-8") as archivo:
        contenido = archivo.read()
        resultado = '#'.join(contenido)
        print(resultado)
hash_display()