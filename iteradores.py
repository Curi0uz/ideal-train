# Ejemplo de Iterador 

# Crear una lista
my_list = [ x for x in range(1,5)]
print(my_list)

# Obten el iterador 
my_iter = iter(my_list)

# Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
