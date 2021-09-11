from typing import BinaryIO
import json


def read_operations(file: BinaryIO):
    print(file.read())
    print(file.readable())
    print(file.readline())
    print(file.readlines())


def write_operations(file: BinaryIO):
    print(file.write("hola"))
    print(file.write("adios"))
    print(file.writable())
    print(file.writelines([]))


def read_json(file):
    data = json.load(file)
    return data


def write_json(diccionario):
    json_object = json.dumps(diccionario)
    print(type(json_object))
    f = open("sample.json", "w")
    f.write(json_object)
    f.close()


if __name__ == "__main__":
    alumnos = {
        "alumnos": [
            {"nombre": "Jose", "escuela": "escom"},
            {"nombre": "Jose", "escuela": "escom"}
        ]
    }
    write_json(alumnos)