# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):

    multiplier = 1

    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
       
multiplication_table(3)  
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum(a, b):
    return a + b
result = sum(3, 4)
print("Сума ", result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    return sum(numbers) / len(numbers)

my_list = [4, 7, 10, 3]
result = average(my_list)
print("Середнє арифметичне:", result)
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(my_string):
    return my_string[::-1]

result = reverse("Glory to Ukraine")
print(result)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

my_words = ["book", "table", "jhdbvghdbv", "dog"]
result = longest_word(my_words)
print("Найдовше слово ", result)
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
      return str1.index(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""
Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_elements = [x for x in small_list if small_list.count(x) == 1]
print(unique_elements)
"""
def unique_elements(lst):
    return [x for x in lst if lst.count(x) == 1]
small_list = [3, 1, 4, 5, 2, 5, 3]
find_elements = unique_elements(small_list)
print(find_elements)

# task 8
"""
=== Перевірка паролю ==="
password = input("Введіть ваш пароль: ")
if len(password) >= 8:
    print("Пароль прийнято!")
else:
    print("Помилка: пароль повинен містити 8 символів.")
"""
def password_check (password):
    if len(password) >= 8:
       return "Пароль прийнято!"
    else:
       return "Помилка: пароль повинен містити 8 символів."
    
user_password = input("Введіть ваш пароль: ")
result = password_check(user_password)
print(result)

# task 9
""" 
Високосний рік
Рік є високосним, якщо:
Ділиться на 4 І не ділиться на 100"
- АБО ділиться на 400
year = 2025
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      print (year, " is a leap year")
else :
      print(year, "is not a leap year")  
"""
def leap_year (year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year"
    else :
      return f"{year} is not a leap year"
    
my_year = 1995 
result = leap_year(my_year) 
print(result)
# task 10
""" Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
while True:
    pizza_topping = input("Add pizza topping or 'quit' to stop):").lower()
    if pizza_topping == 'quit':
        print("Preparing you pizza")
        break
    else:
        print(f"Adding {pizza_topping} to your pizza.")
 """

def pizza_topping(topping):
    if topping == 'quit':
        return "Preparing you pizza"
    else:
        return f"Adding {topping} to your pizza."
    
user_topping = input("Add pizza topping or 'quit' to stop: ").lower()
result = pizza_topping(user_topping)
print(result)   

    
    