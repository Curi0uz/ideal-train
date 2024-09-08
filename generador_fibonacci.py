#Fibonacci
# 0 1 1 2 3 5 8 13 21...

def fibonacci(limit):
    a, b = 0, 1
    while a<limit:
        yield a
        a, b = b, a+b

#for num in fibonacci(15):
    #print(num)

def impares(limite):
    a = 1
    while a<limite:
        a = a+2
        yield a

for n in impares(10):
    print(n)