'''
Crea una clase virtual llamada Algoritmo con los
atributos nombre, tarea y aprendizaje que sea
superclase de la clase BaseClassifier del
problema anterior. Comprueba con el método
issubclass que Algoritmo es padre de
BaseClassifier.
'''
from abc import ABCMeta
class BaseClassifier:
    def __init__(self):
        pass

class Algoritmo(metaclass=ABCMeta):
    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje
Algoritmo.register(BaseClassifier)
print(issubclass(BaseClassifier, Algoritmo))
        