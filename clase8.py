to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "volver al hotel"]
print(to_do)
numbers = [1,2,3,4,"cinco"]
print(type(numbers))
mix = ["uno",2,3.14,True,[1,2,3]]
print(mix)
print("Primer Elemento:",mix[0])
print("Ultimo elemento:",mix[-1])
print(mix[0:2])
print(mix[2:-2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1,2,100.01,90.45,3,4,5]
print(numbers)
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
print(numbers)