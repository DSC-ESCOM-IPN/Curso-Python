conjunto = set(["a", "b", "c", "a"])
conjunto1 = {"a", "b", "c"}

print("Imprimir set:")
print(conjunto)
print("--------------------------------------------")

print("Agregar elemento:")
conjunto.add('d') 
print(conjunto)
print("--------------------------------------------")

print("Agregar elementos:")
conjunto.update({"a", "g"}) 
print(conjunto)
print("--------------------------------------------")

print("Longitud:")
print(len(conjunto))
print("--------------------------------------------")

print("Eliminar elemento:")
conjunto.discard('g')
conjunto.discard('h')
print(conjunto)
print("--------------------------------------------")

print("Eliminar ultimo elemento:")
conjunto.pop()
print(conjunto)
print("--------------------------------------------")

print("Busqueda:")
print('a' in conjunto)
print("--------------------------------------------")

print("Vaciar Conjunto:")
conjunto.clear()
print(conjunto)
print("--------------------------------------------")

#Operaciones con otros conjuntos union(), update(), difference(), intersection(), issubset(), etc
frozen_set = frozenset(["a", "b", "c"])
lista = [1,2,1,2,3,4,5,6,7,8,3]
print(set(lista))
