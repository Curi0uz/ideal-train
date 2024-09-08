# Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos.
#  Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno.
#  Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.

#Consecionaria


#Vehiculo
class Car:
    def __init__(self, brand, year, value):
        self.brand = brand
        self.year = year
        self.value = value
        self.available = True
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"El vehiculo {self.brand} del año {self.year} ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}, del año {self.year} no se encuentra disponible")

    def buy(self):
        if self.available:
            

class Client:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def buy_car(self,car):
        if car.available:




class Consessionary:
    def __init__(self):
        self.buys = []
        self.sells = []



# Crear objetos
car1 = Car("Toyota", 2004, 5000)

#Llamar a los metodos
car1.sell()