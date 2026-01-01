'''
Crea una clase Car que herede de Vehicle y que
sobreescriba los métodos max_speed() y
change_gear(). Instancia dos objetos de cada
clase y compruebaque la salida de cada método
es distinta
'''
class Vehicle:
    def __init__ (self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        print('Details:', self.name, self.color, self.price)
    def max_speed(self):
        print('Vehicle max speed is 150')
    def change_gear(self):
        print('Vehicle change 6 gear')
class Car(Vehicle):
    def __init__(self, name, color, price):
        super().__init__(name, color, price)
    def max_speed(self):
        print('Car max speed is 250')
    def change_gear(self):
        print('Car change 8 gear')
v1 = Vehicle('Truck', 'Red', 20000)
v1.show()
v1.max_speed()
v1.change_gear()
c1 = Car('BMW', 'Black', 50000)
c1.show()
c1.max_speed()
c1.change_gear()