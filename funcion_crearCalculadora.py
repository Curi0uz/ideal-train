# Crear funciones para realizar las operaciones
def add(a,b):
    return(a+b)

def substract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

# Crear una funcion calculadora que ocupe las demas funciones

def calculadora():
    
    while True:
        print("1.Sumar:")
        print("2.Restar:")
        print("3.Multiplicar:")
        print("4.Dividir:")
        print("5.Salir de la calculadora:")

        option = input("Ingresa tú opción(1,2,3,4,5):")
        
        if option == "5":
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("ingresa el primer numero:"))
            num2 = float(input("ingresa el segundo numero:"))

        if option == "1":
            print("La suma resultante es:", add(num1,num2))
        elif option == "2":
            print("La resta resultante es:",substract(num1,num2))
        elif option == "3":
            print("La Multiplicación resultante es:", multiply(num1,num2))
        elif option == "4":
            print("La division resultante es:", divide(num1,num2))                  
        else:
            print("por favor elige un numero valido")


calculadora()