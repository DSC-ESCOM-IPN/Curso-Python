def operaciones(a,b):
  suma = a+b
  resta = a-b
  mult = a*b
  div = a/b
  return (suma,resta,mult,div)

def my_num(num2, num, num3):
  return ("Numero vale:",num)

def carros(dict):
  for key in dict: 
        print("Llave:", key, "Valor:", dict[key])

print("------------------------------------------------------------")
suma, resta, _, div = operaciones(10,6)
print(suma)
print(resta)
print(div)
print("------------------------------------------------------------")
print(my_num(num3=1, num2=4, num=20))
print("------------------------------------------------------------")

print("------------------------------------------------------------")
carros({'Ferari':'F40','chevrolet':'camaro'})