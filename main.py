class Animal:

    def __init__(self, color, tipo="perro") -> None:
        self.color = color
        self.tipo = tipo

    def format_animal(self):
        print("El animal es de color"+ str(self.color)+ ", y tipo" +str(self.tipo))
        print("El animal es de color{1} , y tipo{0}".format(self.tipo, self.color))
        return f"El animal es de color{self.color}, y tipo {self.tipo}"


animal1 = Animal(color="cafe")

print(animal1.format_animal())

