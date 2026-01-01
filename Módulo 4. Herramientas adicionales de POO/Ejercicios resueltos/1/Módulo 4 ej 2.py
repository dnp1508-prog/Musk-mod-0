'''
Representa el siguiente diagrama con sus clases,
atributos y métodos correspondientes.
Cada método display debe imprimir el nombre de
la clase, atributos y valores de la instancia en ese
momento. Ejemplo: In
displaymethodofParent1x=10
'''

class Parent1():
    def __init__(self, name1):
        self.name1 = name1
    def display(self):
        print('{}'.format(self.name1))
class Parent2():
    def __init__(self, name2):
        self.name2 = name2
    def display(self):
        print('{}'.format(self.name2))
class Child(Parent1, Parent2):
    def __init__(self, name1, name2, name3):
        Parent1.__init__(self, name1)
        Parent2.__init__(self, name2)
        self.name3 = name3
    def display(self):
        print('{} es hijo de {} y {}'.format(self.name3, self.name1, self.name2))
child1 = Child('josé', 'Ana', 'Juan')
child1.display()