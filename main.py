import json
# Escribe una funcion que reciba el archivo file.json obtenga el nombre y promedio
# de todas las personas y regrese el nombre de la persona con mayor promedio
def person_with_highest_average(fileName: str) -> str:      
    mayor = 0.0
    listapromedios = []
    listanombres = []
    with open(fileName) as file:
        data = json.load(file)
    
    for alumno in data['alumnos']:
        listanombres.append(alumno['nombre'])
        for prom in alumno['calificaciones']:
            listapromedios.append(prom['promedio'])
            if float(prom['promedio']) > mayor:
                mayor = float(prom['promedio'])
    posicion = listapromedios.index(str(mayor)) 
    return listanombres[posicion]
    
# Escribe una funcion que reciba el archivo file.json ordene a las personas y
# las escriba en un nuevo archivo alumnos.txt en orden de promedio de menor a mayor
# su nombre seguido de la longitud de caracteres del nombre removiendo espacios
# Ejemplo (alumnos.txt)
# alum-1 6
# example-a 9
# format-1b2a 11
# examples-c 10
def sort_people_by_average_in_file(fileName: str) -> None:
    pass


# Escribe un programa que cuente el numero de ocurrencias de la palabra python en el archivo file.txt
def count_number_ocurrences_word(fileName: str) -> int:
    contador_python = 0

    documento = open(fileName, "r")
    archivocompleto = documento.read()
    archivosincomas = archivocompleto.replace(",", "")
    archivo = archivosincomas.replace(".", "")
    palabras = archivo.split()
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra == "python":
            contador_python += 1  

    return contador_python



# Escribe un programa que cuente el numero de palabras en el archivo words.txt
def count_words(fileName: str) -> int:
    documento = open(fileName, "r")
    palabras = documento.read()
    numerodepalabras = palabras.split()
    return len(numerodepalabras)