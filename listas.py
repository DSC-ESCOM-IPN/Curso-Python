lista = ['String',123,1.23,True]
otraLista = ['A','1','C','D','%']
listaEnLista = ['1','2',lista]

print('Imprimir listas:')
print(lista)
print('Lista dentro de lista')
print(listaEnLista)
print("--------------------------------------------")

print("Agregar elemento:")
lista.append("elemento")
print(lista)
print("--------------------------------------------")

print("Agregar elemento en una posicion:")
lista.insert(2,'NuevoElemento')
print(lista)
print("--------------------------------------------")

print("Eliminar un elemento:")
lista.remove("NuevoElemento")
print(lista)
print("--------------------------------------------")

print("Eliminar el ultimo elemento:")
print("Elemento eliminado:{}".format(lista.pop()))
print("--------------------------------------------")

otraLista = ['A','1','C','D','%']
print("Slices:")
print(otraLista[1:3])
print(otraLista[:2])
print(otraLista[1:])
print(lista+otraLista)
print("--------------------------------------------")

print("Multiplicacion:")
print(lista*4)
print("--------------------------------------------")

print("Busqueda:")
print('String' in lista)
print('A' in lista)
print("--------------------------------------------")

print("Indice elemento:")
print(lista.index(123))