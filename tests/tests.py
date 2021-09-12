import main as test_functions
import filecmp


def test_person_with_highest_average():
    assert test_functions.person_with_highest_average("file.json") == "Jaime Lopez"


def test_sort_people_by_average_in_file():
    test_functions.sort_people_by_average_in_file("file.json")
    file1 = "alumnos_result.txt"
    file2 = "alumnos.txt"
    assert filecmp.cmp(file1, file2) == True


def test_count_number_ocurrences_word():
    assert test_functions.count_number_ocurrences_word("file.txt") == 13


def test_count_words():
    assert test_functions.count_words("words.txt") == 80
