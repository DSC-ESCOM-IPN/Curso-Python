from typing import Dict, List, Tuple
import datetime

# Escribe una funcion que regrese el valor de fibonacci en la posicion nth
def fibonacci(n: int) -> int:
    # aqui escribe tu funcion
    return 1


# Escribe una funcion que verifique si una cadena es anagrama de otra
def is_anagram(str1: str, str2: str) -> bool:
    # aqui escribe tu funcion
    pass


# Escribe una funcion que regrese los numeros impares entre 0-100
def first_100_odd_numbers() -> List[int]:
    result = []
    for i in range(0, 100):
        if i % 2 != 0:
            result.append(i)
    return result


# Escribe una funcion que convierta un numero decimal a binario
def decimal_to_binary(n: int) -> str:
    pass


# Escribe una funcion que recibe una lista de enteros y un valor n, que regrese
# el indice de los dos numeros que suman dicho valor n
def two_sum(numbers: List[int], target: int) -> List[int]:
    pass


# Escribe una funcion que regrese el numero mayor y menor de un diccionario
# {"key1": 3, "key2": -1, "key1": 20, "key1": 4} min=-1 max=20
# (min, max)
def max_and_min_value_in_dict(values: Dict) -> Tuple[int, int]:
    pass

# Escribe una funcion que ordene numeros
def sort_numbers(nums: List[int]) -> List[int]:
    pass
