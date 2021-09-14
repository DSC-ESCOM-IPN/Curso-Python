from typing import Dict, List, Tuple


# Escribe una funcion que regrese el valor de fibonacci en la posicion nth
def fibonacci(n: int) -> int:
    actual =0;ant=0;sig =1
    for i in range(0,n-1):
        actual = ant + sig
        ant = sig
        sig = actual
    return actual



# Escribe una funcion que verifique si una cadena es anagrama de otra
def is_anagram(str1: str, str2: str) -> bool:
    a = sorted(str1)
    b = sorted(str2)
    return a==b


# Escribe una funcion que regrese los numeros impares entre 0-100
def first_100_odd_numbers() -> List[int]:
    arre = list()
    for i in range(1,100,2):
        arre.append(i)
    return arre


# Escribe una funcion que convierta un numero decimal a binario
def decimal_to_binary(n: int) -> str:
    return format(n, "b")


# Escribe una funcion que recibe una lista de enteros y un valor n, que regrese
# el indice de los dos numeros que suman dicho valor n
def two_sum(numbers: List[int], target: int) -> List[int]:

    for i in numbers:
        a = {}
        for i, val in enumerate(numbers):
            num = target - val
            if num in a:
                return [a[num],i]
            a[val] = i


# Escribe una funcion que regrese el numero mayor y menor de un diccionario
# {"key1": 3, "key2": -1, "key1": 20, "key1": 4} min=-1 max=20
# (min, max)
def max_and_min_value_in_dict(values: Dict) -> Tuple[int, int]:
    maxi = -1; mini = 0
    for x in values:
        if values[x] > maxi:
            maxi = values[x]
        if values[x] < mini:
            mini = values[x]
    ans = (mini,maxi)
    return ans

# Escribe una funcion que ordene numeros
def sort_numbers(nums: List[int]) -> List[int]:
    nums.sort()
    return nums