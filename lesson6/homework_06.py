# Вправа 1: Проста математика
print("\n=== ВПРАВА 1: Калькулятор ===")
print("Створіть простий калькулятор для двох чисел і двох дій")
print("Підтримувані операції: +, -")

# Початок реалізації:
num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, ): ")
num2 = float(input("Введіть друге число: "))
if operation == "+":
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
elif operation == "-":
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
else:
        print("Помилка: непідтримувана операція.")

# Вправа 2: Перевірка паролю
print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")
password = input("Введіть ваш пароль: ")
if len(password) >= 8:
    print("Пароль прийнято!")
else:
    print("Помилка: пароль повинен містити 8 символів.")


# Вправа 3: Визначення високосного року
print("\n=== ВПРАВА 3: Високосний рік ===")
print("Рік є високосним, якщо:")
print("- Ділиться на 4 І не ділиться на 100")
print("- АБО ділиться на 400")
year = 2025
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      print (year, " is a leap year")
else :
      print(year, "is not a leap year")      
    

# Вправа 4: Лічильник голосних
print("\n=== ВПРАВА 4: Лічильник голосних ===")
print("Підрахуйте кількість голосних у рядку")

text = input("Введіть текст: ").lower()
lowels = "аеиіїоуюя"
count = 0
for letters in text :
    if letters in lowels:
        count +=1

print(f"Кількість голосних: {count}")


# Вправа 5: Гра 
print("\n=== ВПРАВА 5: Гра ===")
"""
Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо колір прибульця green, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця yellow, надрукуйте, що гравець щойно заробив 10 балів.
Якщо колір прибульця red - надрукуйте, що гравець щойно заробив 15 балів.
Перевірте роботу гри самостійно, змінюючи значення alien_color
"""
alien_color = "green"
if alien_color ==  "green" :
      print ("you won 5 points")
elif alien_color == "yellow"  :
      print("you won 10 points")
elif alien_color == "red" :
      print("you won 15 points")
else:
      print("unknown color")      
         


# Вправа 6: Піцерія *
print("\n=== ВПРАВА 6: Начинки для піци (pizza_topping) ===")
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
while True:
    pizza_topping = input("Add pizza topping or 'quit' to stop):").lower()
    if pizza_topping == 'quit':
        print("Preparing you pizza")
        break
    else:
        print(f"Adding {pizza_topping} to your pizza.")


# Вправа 7: Зворотний порядок цифр
print("\n=== ВПРАВА 7: Зворотний порядок ===")
print("Виведіть цифри числа у зворотному порядку")

number = input("Введіть число: ")
reversed_number = number[::-1]
print("reversed number is ", reversed_number)

# Вправа 8: Пошук максимального числа
print("\n=== ВПРАВА 8: Пошук максимального ===")
print("Знайдіть найбільше число серед введених")
print("Введіть 0 для завершення")
max_number = None
while True:
    num = int(input("add number: "))
    if num == 0:
        break 
    if (max_number is None) or (num > max_number):
        max_number = num
print(f"the biggest number is : {max_number}")          

# Вправа 9: Виключення зі списку
print("\n=== ВПРАВА 9: Виключення зі списку ===")
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == "orange":
        continue 
    print(fruit)


# Вправа 10: Вираз в один рядок
print("\n=== ВПРАВА 10: Вираз з умовою в один рядок ===")
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x**2 for x in numbers if x % 2 == 0]
print(result) 