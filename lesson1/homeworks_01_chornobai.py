# task 01 == Виправте синтаксичні помилки
print("Hello")
print("world!")

# task 02  == Виправте назви змінних, щоб текст виводався
first_wold = "Hello"
second_wold = "world"
print(first_wold,second_wold)

# task 03 == Зробіть так, щоб кількість бананів була
# завжди на чотири штуки більша, ніж яблук
apples = 2
banana = apples + 4


# task 04 == виправте назви змінних
page_1 = 1
page_2 = 2
page_3 = 3
page_4 = 4

# task 05 == Порахуйте периметр фігури з task 04
# та виведіть його для користувача
#я порахувала для паралелограма бо формула для трикутника буде інша 
side_a = 2
side_b = 3
perimetery = 2 * (side_a + side_b)
print(perimetery)


"""
    # Задачі 06 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 06
"""
У Оксани було 20 марок із серії «Мистецтво» 
і 7 марок із серії «Звірі».
5 марок із серії «Мистецтво» та
1 марку із серії «Звірі» вона подарувала подружці. 
Скільки марок лишилось у Оксани?
"""
animals_mark = 7
art_marks = 20
Oksana_total_mark = print(animals_mark - 1 + art_marks - 5)

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pears_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = print(apple_trees + pears_trees + plum_trees,"trees")
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temperature = 5
midday_temperature = morning_temperature - 10
evening_temperature = midday_temperature + 4
print(evening_temperature, "degrees") 
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_total = 24
girls_total = boys_total/2
children_total = print(boys_total - 1 + girls_total - 2,"children")
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1_price = 8
book_2_price = book_1_price + 2
book_3_price = (book_1_price + book_2_price)/2
total_books_price = print(book_1_price + book_2_price + book_3_price,"UAN")