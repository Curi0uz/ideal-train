add = lambda a, b: a+b
print(add(10,4))

multiply = lambda a, b: a*b
print(multiply(4,20))

# Cuadrado de cada numero
numbers = range(0,11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("cuadradors", squared_numbers)

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Pares:", even_numbers)