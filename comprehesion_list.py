squares = [x**2 for x in range(1,11)]
#print("Cuadrados:", squares)

celsius = [(x * 10) for x in range(0,5)]
print(celsius)

fahrengheit = [(temp * 9/5) *32 for temp in celsius]
print("Temperatura en grados fahrengheit:", fahrengheit)

# Numeros pares
evens = [x for x in range(1,21) if x%2 == 0]
#print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0])) ]