# Ejercicio 1
'''
Se ha definido una clase relativa al inventario de un jet imaginario.
También se ha creado una instancia de esta clase Jet.
Imprime el primer atributo de la instancia.
'''

class Jet:

    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jet('F16', 'USA')
print(first_item.name)

# Ejercicio 2
'''
Usando la clase Jet, crea nuevas instancias con los siguientes nombres y orígenes
'''

class Jet:

    def __init__(self, name, country):
        self.name = name
        self.origin = country

    def rep(self):
        return(self.name, self.origin)

def rep(lista):
    for i in lista:
        jet = (Jet(i[0], i[1]))
        print(jet.rep())
lista = [('F16', 'USA'), ('SU33', 'Russia'), ('AJS37', 'Sweden'),
        ('MIRAGE2000', 'France'), ('F14', 'USA'), ('Mig29', 'USSR'),
        ('A10', 'USA')]
rep(lista)

# Ejercicio 3
'''
Añade otro atributo llamado "Cantidad" a la clase.
El usuario le dará valor pasando un nuevo parámetro por el constructor.
A continuación, crea 2 instancias para F14 y Mirage2000 con las cantidades 87 y 35.
'''

class Jet:

    def __init__(self, name, country, cantidad):
        self.name = name
        self.origin = country
        self.cantidad = cantidad

    def rep(self):
        return(self.name, self.origin, self.cantidad)

first_item = Jet('F14', 'USA', 87)
second_item = Jet('Mirage2000', 'France', 35)
print(first_item.rep())
print(second_item.rep())

# Ejercicio 4
'''
Dada la siguiente instancia y sus atributos, crea una clase que la instancie.
'''

class Nobel:
    
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

np2005 = Nobel("Peace", 2005, 'Muhammad Yunus')
print(np2005.category, np2005.year, np2005.winner)

# Ejercicio 5
'''
Crea una clase con el nombre de 'Estudiante', e inicialica atributos como el nombre,
la edad y el grado mientras crea un objeto.
'''

class Estudiante:

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

estudiante1 = Estudiante('David', 17, '2º de Bachillerato')

# Ejercicio 6
'''
Escribe un programa para crear una clase vacía valida con el nombre de 'Estudiante',
sin propiedades.
'''

class Estudiante:
    pass

# Ejercicio 7
'''
Añade un método público en la clase 'Estudiante' que calcule la media de una lista
de notas y actualiza el valor del atributo grade. A continuación llama a la función
en tu programa principal e imprime el valor de grade.
'''

class Estudiante:

    def __init__(self, nombre, edad, grado, grade):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.grade = grade
    def media(self, grade):
        self.grade = sum(grade)//len(grade)
        return(self.grade)
Nombre = input('Introduce tu nombre: ')
Edad = int(input('Introduce tu edad: '))
Curso = input('Introduce tu curso: ')
n = int(input('introduce el número de notas: '))
grade = []
for i in range(n):
    nota = float(input('Introduce la nota {}: '.format(i+1)))
    grade.append(nota)
estudiante1 = Estudiante(Nombre, Edad, Curso, grade)
print(estudiante1.media(grade))

# Ejercicio 8
'''
Añade a la clase anterior un método estático que dada una lista de notas
y sus asignaturas asociadas como diccionatio imprima aquellas asignaturas que han
recibido un nota inferior a 5.
'''

class Estudiante:

    def __init__(self, nombre, edad, grado, grade):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.grade = grade
        
    def media(self, grade):
        self.grade = sum(grade)//len(grade)
        return(self.grade)
    
    @staticmethod
    def suspensos(notas):
        for asignatura, nota in notas.items():
            if nota < 5:
                print('Has suspendido {} con un {}'.format(asignatura, nota))

n = int(input('introduce el número de notas: '))
materias = []
grades = []
for i in range(n):
    materia = input('Introduce la asignatura: ')
    materias.append(materia)
    nota = float(input('Introduce la nota: '))
    grades.append(nota)
notas = dict(zip(materias, grades))
Estudiante.suspensos(notas)

# Ejercicio 9
'''
Añade un atributo de clase llamado escuela a la clase "Estudiante" y dale un
valor predeterminado. A continuacón, añade un método de clase que dado el nombre
de otra escuela actualice el valor de ese atributo. Llama a tu método en el programa
principal y asegúrate de que funciona.
'''

class Estudiante:

    escuela = 'Pompeu Fabra'
    
    def __init__(self, nombre, edad, grado, grade):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.grade = grade

    @classmethod
    def nueva_escuela(cls, new_escuela):
        escuela = new_escuela
        return (escuela)
estudiante1 = Estudiante.nueva_escuela('INS Ramón Coll i Rodés')
print(estudiante1)

# Ejercicio 10
'''
Añade un método privada en la clase anterior que dado un diccionario mes-número
de asistencias, devuelva 1 si algún mess tiene una asistencia < 4, devuelva 2
si algún mes tiene una asistencia entre [4,8) o bien devuelva 3 en caso contrario.
Para probar el método privado, encapsúlalo con una funcion pública que devuelva
su resultado.
'''

class Estudiante:
    
    def __init__(self, nombre, edad, grado, grade):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.grade = grade

    def __asistencias(self, mes_número):
        resultados = []
        for mes, asistencia in mes_número.items():
            if asistencia < 4:
                resultados.append(1)
            elif 4 <= asistencia < 8:
                resultados.append(2)
            else:
                resultados.append(3)
        return min(resultados)
    
    def rep(self, mes_número):
        return self.__asistencias(mes_número)

estudiante1 = Estudiante('David', 17, '2º', 9)
datos_asistencia = {
    "enero": 8,
    "febrero": 2,
    "marzo": 10 }
res = estudiante1.rep(datos_asistencia)
print('{}'.format(res))
