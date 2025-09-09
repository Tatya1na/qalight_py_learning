
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent
sys.path.insert(0,str(root_dir))
from lesson_11.home.functions_for_test import *

"""
📝 Завдання 1. Перевірка додавання чисел 
Напиши тест на функцію add(a, b), яка повертає суму двох чисел. 
Створи тест, який перевіряє кілька випадків: додавання додатних, від’ємних і нуля.
"""
def test_add_positive_numbers():
    actual_result = add(2, 3)
    expected_result = 5
    assert actual_result == expected_result

def test_add_negative_numbers():
    actual_result = add(-4, -6)
    expected_result = -10
    assert actual_result == expected_result

def test_add_zero_and_number():
    actual_result = add(0, 7)
    expected_result = 7
    assert actual_result == expected_result

def test_add_positive_and_negative():
    actual_result = add(10, -3)
    expected_result = 7
    assert actual_result == expected_result

def test_add_zero():
    actual_result = add(-1, 0)
    expected_result = -1
    assert actual_result == expected_result

"""
📝 Завдання 2. Перевірка парності 
Функція is_even(n) повертає True, якщо число парне, інакше False. 
Напиши тести для кількох чисел: парних, непарних, від’ємних.
"""
def test_is_even_even():
    actual_result = is_even(6)
    expected_result = True
    assert actual_result == expected_result

def test_is_even_odd():
    actual_result = is_even(5)
    expected_result = False
    assert actual_result == expected_result

def test_is_even_odd():
    actual_result = is_even(-1)
    expected_result = False
    assert actual_result == expected_result
"""
📝 Завдання 3. Розворот рядка 
Функція reverse_string(s) повинна повертати рядок у зворотному порядку. 
Перевір: звичайний рядок, порожній рядок, рядок з одним символом.
"""
def test_reverse_string():
    actual_result = reverse_string("Hello string")
    expected_result = "gnirts olleH"
    assert actual_result == expected_result

def test_reverse_string_empty():
    actual_result = reverse_string("")
    expected_result = ""
    assert actual_result == expected_result    

def test_reverse_string_symbol():
    actual_result = reverse_string("@")
    expected_result = "@"
    assert actual_result == expected_result

"""
📝 Завдання 4. Мінімум у списку 
Функція find_min(nums) повертає найменший елемент списку. 
Протестуй для: звичайного списку, списку з одним елементом, списку з від’ємними числами.
"""
def test_find_min_normal_list():
    assert find_min([3, 1, 4, 2]) == 1

def test_find_min_single_element():
    assert find_min([42]) == 42

def test_find_min_with_negative_numbers():
    assert find_min([-5, -1, -10, 0]) == -10



"""
📝 Завдання 5. Перевірка підрядка 
Функція contains_substring(s, sub) повертає True, якщо sub є в s. 
Протестуй випадки: підрядок є, підрядка нема, порожній підрядок.
"""
def test_contains_substring_found():
    assert contains_substring("hello world", "world") == True

def test_contains_substring_not_found():
    assert contains_substring("hello world", "string") == False

def test_contains_substring_empty_sub():
    assert contains_substring("hello world", "") == True


"""
📝 Завдання 6. Факторіал 
Функція factorial(n) обчислює факторіал числа n. 
Протестуй: factorial(0), factorial(1), factorial(5).
"""
import pytest
def test_factorial_raises_value_error_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_zero():
    actual_result = factorial(0)
    expected_result = 1
    assert actual_result == expected_result

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_five():
    actual_result = factorial(5)
    expected_result = 120
    assert actual_result == expected_result
"""
📝 Завдання 7. Ділення з винятком 
Функція divide(a, b) ділить a на b. 
Перевір: звичайне ділення, ділення на від’ємне число, ділення на нуль (очікуваний ZeroDivisionError).
"""
def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(10, -2) == -5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


"""
📝 Завдання 8. Паліндром 
Функція is_palindrome(s) перевіряє, чи є рядок паліндромом. 
Протестуй: паліндром, непаліндром, порожній рядок.
"""
def test_is_palindrome_true():
    assert is_palindrome("madam") == True

def test_is_palindrome_false():
    assert is_palindrome("hello") == False

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True


"""
📝 Завдання 9. Сума елементів списку 
Функція sum_list(nums) повертає суму всіх чисел у списку. 
Протестуй: звичайний список, порожній список, список з від’ємними числами.
"""
def test_sum_list_normal():
    actual_result = sum_list([1, 2, 3, 4])
    expected_result = 10
    assert actual_result == expected_result

def test_sum_list_empty():
    actual_result = sum_list([])
    expected_result = 0
    assert actual_result == expected_result

def test_sum_list_negative_numbers():
    actual_result = sum_list([-5, -1, 6])
    expected_result = 0
    assert actual_result == expected_result


"""
📝 Завдання 10. Конвертація в верхній регістр 
Функція to_upper(s) повертає рядок у верхньому регістрі. 
Протестуй: звичайний рядок, вже великими літерами, порожній рядок.
"""
def test_to_upper_normal_string():
    actual_result = to_upper("hello world")
    expected_result = "HELLO WORLD"
    assert actual_result == expected_result

def test_to_upper_already_uppercase():
    actual_result = to_upper("PYTHON")
    expected_result = "PYTHON"
    assert actual_result == expected_result

def test_to_upper_empty_string():
    actual_result = to_upper("")
    expected_result = ""
    assert actual_result == expected_result
