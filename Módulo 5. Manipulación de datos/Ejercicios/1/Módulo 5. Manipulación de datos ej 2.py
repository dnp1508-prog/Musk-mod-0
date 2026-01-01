'''
Escribe una función para contar el número de
líneas de un archivo de texto "historia.txt":
Ejemplo: Si el archivo "story.txt" contiene las 
siguientes líneas:
Un niño está jugando allí.
Hay un parque infantil.
Un avión está en el cielo.
El cielo es rosa.
La contraseña puede contener letras y números.
El resultado debe ser 5.
'''
def contar_lineas():
    ubicacion = "history.txt"
    with open(ubicacion, "r", encoding = "utf-8") as archivo:
        lineas = archivo.readlines()
        numero_lineas = len(lineas)
        return numero_lineas

def condicion():
    ubicacion2 = "story.txt"
    with open(ubicacion2, "r", encoding = "utf-8") as archivo2:
        lineas2 = archivo2.readlines()
        condicion = lineas2[0].strip() == "Un niño está jugando allí." and lineas2[1].strip() == "Hay un parque infantil." and lineas2[2].strip() == "Un avión está en el cielo." and lineas2[3].strip() == "El cielo es rosa." and lineas2[4].strip() == "La contraseña puede contener letras y números." and lineas2[5].strip() == "El resultado debe ser 5."
        if condicion:
            return contar_lineas()
print(condicion())
