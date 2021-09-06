import main as test_functions

def test_fibonacci():
    assert test_functions.fibonacci(0) == 0
    assert test_functions.fibonacci(10) == 55
    assert test_functions.fibonacci(5) == 5
    assert test_functions.fibonacci(11) == 89
    assert test_functions.fibonacci(20) == 6765
    assert test_functions.fibonacci(40) == 102334155

def test_anagram():
    assert test_functions.is_anagram("arc", "car") == True
    assert test_functions.is_anagram("act", "cat") == True
    assert test_functions.is_anagram("car", "act") == False
    assert test_functions.is_anagram("saco", "cosa") == True
    assert test_functions.is_anagram("Caja", "cajon") == False


def test_odd_numbers():
    assert test_functions.first_100_odd_numbers() == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]


def test_decimal_to_binary():
    assert test_functions.decimal_to_binary(7) == "111"
    assert test_functions.decimal_to_binary(10) == "1010"
    assert test_functions.decimal_to_binary(24) == "11000"
    assert test_functions.decimal_to_binary(18) == "10010"


def test_two_sum():
    assert test_functions.two_sum([1,2,3,4], 6) == [1, 3]
    assert test_functions.two_sum([4,2,1,5,4], 6) == [2, 3]
    assert test_functions.two_sum([6,7,1,20,3,4,8], 28) == [3, 6]


def test_max_and_min_value_in_dict():
    assert test_functions.max_and_min_value_in_dict({"key1": 3, "key2": -1, "key1": 20, "key1": 4}) == (-1, 20)
    assert test_functions.max_and_min_value_in_dict({"key1": -10, "key2": 4, "key1": 15, "key1": -8}) == (-10, 15)


def test_sort_numbers():
    assert test_functions.sort_numbers([-4,3,6,10,1,-6]) == [-6,-4,1,3,6,10]
    assert test_functions.sort_numbers([20,-3,6,-10,1,6]) == [-10,-3,1,6,6,20]
