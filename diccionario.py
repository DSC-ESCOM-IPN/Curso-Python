dic = {'Hola':'Mundo', 'Key': 'Value', 'Llave':'Valor'}

dic['Hello'] = 'World'

print("Imprimir diccionario:")
print(dic)
print("--------------------------------------------")

print("Obtener valor:")
print(dic['Hola'])
print(dic.get('Hola'))
print("--------------------------------------------")

print("Obtener llaves:")
print(dic.keys())
print("--------------------------------------------")

print("Obtener valores:")
print(dic.values())
print("--------------------------------------------")

print("Eliminar el ultimo elemento:")
print(dic.popitem())
print("--------------------------------------------")

print("Eliminar elemento:")
print(dic.pop('Hola',-1))
print("--------------------------------------------")

print("Longitud:")
print(len(dic))
print("--------------------------------------------")

print("Actualizar valores:")
dic.update([('Llave','NuevoValor'),('Carro','BMW')])
dic["NuevaLlave"] = "NuevoValor"
print(dic)
print("--------------------------------------------")

print("Vaciar diccionario:")
dic.clear()
print(dic)
print("--------------------------------------------")
