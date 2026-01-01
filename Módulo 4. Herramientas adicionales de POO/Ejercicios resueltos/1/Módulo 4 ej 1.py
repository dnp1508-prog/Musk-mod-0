'''
Crea una clase Staff con los atributos role, depty
salary. Crea una clase Profesor que herede de la
clase anterior y que además tenga como
atributos nombre y edad. Haz que sea posible
instanciar un profesor dándole valor a todos los
atributos.
'''
class Staff:
    def __init__(self, role, depty, salary):
        self.role = role
        self.depty = depty
        self.salary = salary

class Professor(Staff):
    def __init__(self, role, depty, salary, nombre, edad):
        super().__init__(role, depty, salary)
        self.nombre = nombre
        self.edad = edad
        x = '{} es {} del departamente de {} con un salario de {} € y tiene {} años'.format(nombre, role, depty, salary, edad)
        print(x)
profesor1 = Professor('Profesor', 'Matemáticas', 3000, 'Juan Pérez', 45)
print(profesor1)
