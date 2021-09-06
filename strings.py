string = "Hola Mundo"
string1 = "Hola"
string2  = " Mundo"

print("Cadena en posicion:")
print(string[0])
print(string[4])
print(string[6])
print("-------------------------------")

print("Concatenar")
print(string1+string2)
print(string1+" Mundo")
string1+= string2
print(string1)
print("-------------------------------")

print("Multiplicar:")
print(string*3)
print("-------------------------------")

print("Slices:")

print(string[2:5])
print(string[0:-2])
print(string[3:])
print(string[::4])
print(string[::-1])
print("-------------------------------")

print("Longitud:")
print(len(string))
print("-------------------------------")

print("Mayusculas|Minusculas:")
print(string.upper())
print(string.lower())
print("-------------------------------")

print("Busqueda:")
print(string.find('Mund'))
print(string.find('World'))
print("-------------------------------")

print("Remplazar:")
print(string.replace('o','a'))
