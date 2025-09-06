"""
### Робота з файлами та папками — завдання

1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
with open("hello.txt", "w") as file:
    file.write("Hello, Python!")

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
with open("hello.txt", "a") as file:
    file.write("Learning file operations.\n")

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
with open("hello.txt", "r") as file:
    for line in file:
        print(line.strip())

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
with open("hello.txt", "r") as file:
    content = file.read()
    print(len(content))

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
import os

os.mkdir("data")                 
with open("data/notes.txt", "w") as file:
    file.write("My first note.\n")

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
print(os.listdir("data"))

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
with open("data/notes.txt", "r") as main_file:
    content = main_file.read()

with open("data/copy.txt", "w") as dest_file:
    dest_file.write(content)

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
with open("a.txt", "w") as file_a:
    file_a.write("Hello a.txt.\n")

with open("b.txt", "w") as file_b:
    file_b.write("world b.txt.\n")

with open("a.txt", "r") as file_a, open("b.txt", "r") as file_b, open("ab.txt", "w") as file_ab:
    content_a = file_a.read()
    content_b = file_b.read()
    file_ab.write(content_a)
    file_ab.write(content_b)

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
with open("notes.txt", "r") as file:
    content = file.read()

if "note" in content:
    print("Знайдено")
else:
    print("Не знайдено")
