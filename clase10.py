numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[1])
information = {"nombre":"Carla",
               "apellido":"Florida",
               "Altura":1.60,
               "Edad": 29}
print(information)
del information["Edad"]
print(information["nombre"])
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)