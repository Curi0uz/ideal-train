try:
    divisor = int(input("Ingresa un numero divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: el divisor no puede ser cero")
    print("Ha ocurrido un error:",e)

except ValueError as e:
    print("Error: Debes introducir un numero valido ")
    print("Ha ocurrido un erro:", e)
