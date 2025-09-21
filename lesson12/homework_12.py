import requests
"""
Написати 50 XPath локаторів для обраного сайту 
"""
site = "rozetka.com.ua"
path = "notebooks"
url = f"https://{site}/{path}"


1. //button[@aria-label='Купити']"
2. //h1[@class='product__title']
3.//div[@class='product-prices__big-price']
4.//div[@class='product-code']
5.//img[@class='product-gallery__image']
6.//div[@class='product-about__description']
7.//div[@class='product-params__list']
8.//div[@class='product-comments__header']
9.//button[@aria-label='Додати до порівняння']
10.//button[@aria-label='Додати до обраного']
11.//div[@class='product-combo']
12.//div[@class='product-combo__item'][1]
13.//div[@class='product-combo__item'][1]//div[@class='product-prices__price']
14.//div[@class='product-combo__item'][1]//a[@class='product-card__title']
15.//div[@class='product-combo__item'][1]//button[@aria-label='Додати до кошика']
16.//div[@class='product-combo__item']
17.//h3[@class='product-combo__title']
18.//a[@class='product-combo__link']
19.//div[@class='product-similar']
20.//div[@class='product-similar__item'][1]
21.//div[@class='product-params__list']
22.//div[@class='product-params__list']//div[@class='product-params__item']
23.//div[@class='product-params__list']//div[@class='product-params__item'][1]
24.//div[@class='product-params__list']//div[@class='product-params__item'][1]//span[@class='product-params__name']
25.//div[@class='product-about__description']
25.//div[@class='product-about__description']//p
26.//div[@class='product-comments__header']
27.//div[@class='product-comments__header']//span[@class='product-comments__count']
28.//div[@class='product-comments__header']//span[@class='product-comments__rating']
29.//div[@class='product-comments__list']
30.//div[@class='product-comments__list']//div[@class='product-comments__item'][1]
31.//div[@class='product-comments__list']//div[@class='product-comments__item'][1]//span[@class='product-comments__author']
32.//div[@class='product-comments__list']//div[@class='product-comments__item'][2]//span[@class='product-comments__author']
33.//div[@class='product-comments__list']//div[@class='product-comments__item'][1]//div[@class='product-comments__text']
34.//div[@class='product-comments__list']//div[@class='product-comments__item'][1]//div[@class='product-comments__text']
35.//div[@class='product-comments__list']//div[@class='product-comments__item'][1]//span[@class='product-comments__date']
36.//div[@class='product-comments__list']//div[@class='product-comments__item'][1]//span[@class='product-comments__likes']
37. //div[contains(@class,"product-about")]
38.//div[contains(@class,"product-about")]/p
39.//input[@type="email"]
40.//button[contains(text(),"Підписатися")]
41.//a/@href
42.//button
43.//img/@src
44.//script/@src
45.//link[@rel="stylesheet"]/@href


