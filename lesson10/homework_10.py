"""
Шаблони класів об'єктів природи та побуту (ЗАГОТОВКИ)
Template classes for nature and household objects (TEMPLATES)

ІНСТРУКЦІЯ / INSTRUCTION:
Реалізуйте всі методи та властивості згідно з вимогами в коментарях
Implement all methods and properties according to requirements in comments
"""

import math


class Tree:
    """
    Клас природного об'єкта "Дерево"
    Class for natural object "Tree"

    Створіть клас природного об'єкта "Дерево". Клас повинен мати наступні атрибути:
- `висота` (висота дерева в метрах)
- `діаметр_стовбура` (діаметр стовбура в см)
- `кількість_листя` (приблизна кількість листя)

Необхідно реалізувати наступні вимоги:
- Значення `висота` повинно бути більше 0 і менше 150 метрів
- Значення `діаметр_стовбура` повинно бути більше 0 і менше 1000 см
- `кількість_листя` обчислюється автоматично за формулою: `висота * діаметр_стовбура * 100`
- Додайте методи:
  - `ріст()` - збільшує висоту на 0.5 м та діаметр стовбура на 2 см
  - `опадання_листя()` - зменшує кількість листя на 30%
  - `інформація()` - виводить всі характеристики дерева
    
    Атрибути / Attributes:
    - height: висота дерева (0 < height < 150 метрів)
    - trunk_diameter: діаметр стовбура (0 < diameter < 1000 см)
    - leaf_count: кількість листя (обчислюється автоматично)
    
    """
    
    def __init__(self, height, trunk_diameter):
        self._height = None
        self._trunk_diameter = None
        self._leaf_count = 0

        self.trunk_diameter = trunk_diameter
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not (0 < value < 150):
            raise ValueError("Висота повинна бути більше 0 і менше 150 метрів.")
        self._height = value
        if self._trunk_diameter is not None:
            self._leaf_count = self._calculate_leaf_count()

    @property
    def trunk_diameter(self):
        return self._trunk_diameter

    @trunk_diameter.setter
    def trunk_diameter(self, value):
        if not (0 < value < 1000):
            raise ValueError("Діаметр стовбура повинен бути більше 0 і менше 1000 см.")
        self._trunk_diameter = value
        if self._height is not None:
            self._leaf_count = self._calculate_leaf_count()

    @property
    def leaf_count(self):
        return self._leaf_count

    def _calculate_leaf_count(self):
        return self._height * self._trunk_diameter * 100

    def grow(self):
        if self.height + 0.5 < 150:
            self.height += 0.5
        else:
            print("Максимальна висота досягнута.")

        if self.trunk_diameter + 2 < 1000:
            self.trunk_diameter += 2
        else:
            print("Максимальний діаметр стовбура досягнуто.")

        print("Дерево виросло.")

    def leaf_fall(self):
        self._leaf_count *= 0.7
        print("Опало 30% листя.")

    def get_info(self):
        return (
            f"Висота: {self.height:.2f} м\n"
            f"Діаметр стовбура: {self.trunk_diameter:.2f} см\n"
            f"Кількість листя: {int(self.leaf_count)} шт."
        )



    
    
class Kettle:
    """
    Клас побутового об'єкта "Чайник"
    Class for household object "Kettle"
    
    Атрибути / Attributes:
    - volume: максимальний об'єм (0.5 <= volume <= 5 літрів)
    - current_volume: поточний об'єм води (0 <= current <= volume)
    - water_temperature: температура води (за замовчуванням 20°C)
    - is_on: чи включений чайник (за замовчуванням False)
    """
    
    def __init__(self, volume):
        self._volume = None
        self._current_volume = 0
        self._water_temperature = 20
        self._is_on = False
        self.volume = volume
    
    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, value):
        if not (0.5 <= value <= 5):
            raise ValueError("Обʼєм повинен бути від 0.5 до 5 літрів")
        self._volume = value
    
    @property
    def current_volume(self):
        return self._current_volume
    
    @property
    def water_temperature(self):
        return self._water_temperature
    
    @property
    def is_on(self):
        return self._is_on
    
    def pour_water(self, amount):
        if amount < 0:
            raise ValueError("Не можна додати відʼємну кількість води")
        
        available_space = self._volume - self._current_volume
        if amount > available_space:
            self._current_volume = self._volume
            print(f"Чайник переповнений! Налито лише {available_space:.2f} л з {amount:.2f} л")
        else:
            self._current_volume += amount
            print(f"Додано {amount:.2f} л води. Поточний обʼєм: {self._current_volume:.2f} л")
    
    def drain_water(self, amount):
        if amount < 0:
            raise ValueError("Не можна зливати відʼємну кількість води.")
        if amount > self._current_volume:
            print(f"Злито лише {self._current_volume:.2f} л")
            self._current_volume = 0
        else:
            self._current_volume -= amount
            print(f"Злито {amount:.2f} л води. Залишилось: {self._current_volume:.2f} л")

    def turn_on(self):
        if self._current_volume > 0:
            self._is_on = True
            self._water_temperature = 100
            print("Чайник увімкнено. Вода закипіла")
        else:
            print(" Немає води. Додайте воду перед вмиканням")
    

    def turn_off(self):
        self._is_on = False
        print("Чайник вимкнено.")

    def get_status(self):
        return (
            f" СТАТУС ЧАЙНИКА:\n"
            f"Обʼєм: {self._volume:.2f} л\n"
            f"Поточна кількість води: {self._current_volume:.2f} л\n"
            f"Температура води: {self._water_temperature}°C\n"
            f"Стан: {'УВІМКНЕНО' if self._is_on else 'ВИМКНЕНО'}"
        )


class Cloud:
    
    

    """
    Клас природного об'єкта "Хмара"
    Class for natural object "Cloud"
    
    Атрибути / Attributes:
    - area: площа хмари (1 <= area <= 10000 км²)
    - altitude: висота над землею (0.5 <= altitude <= 15 км)
    - humidity_density: щільність вологи (0 <= humidity <= 30 г/м³)
    - rain_probability: ймовірність дощу (обчислюється автоматично)
    """
    
    def __init__(self, area, altitude, humidity_density):
        self._area = None
        self._altitude = None
        self._humidity_density  = None
        self._rain_probability = 0

        self.area = area
        self.altitude = altitude
        self.humidity_density = humidity_density
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, value):
        if not (1 <= value <= 10000):
            raise ValueError("Площа має бути від 1 до 10000 км²")
        self._area = value

    @property
    def altitude(self):
        return self._altitude
    
    @altitude.setter
    def altitude(self, value):
        if not (0.5 <= value <= 15):
            raise ValueError ("Висота над землею має бути від 1 до 15 км")
        self._altitude = value
    
    @property
    def humidity_density(self):
        return self._humidity_density
    
    
    @humidity_density.setter
    def humidity_density(self, value):
        if not (0 <= value <= 30):
            raise ValueError("Щільність вологи має бути в межах від 0 до 30 г/м³")
        self._humidity_density = value
        self._rain_probability = self._calculate_rain_probability()
    
    @property
    def rain_probability(self):
      return self._rain_probability
    
    def _calculate_rain_probability(self):
        return min(self._humidity_density * 3, 100)

    def accumulate_moisture(self, amount):
        if amount < 0:
            raise ValueError("Кількість вологи не може бути від'ємною.")
        new_value = min(self._humidity_density + amount, 30)
        self.humidity_density = new_value
        print(f"Хмара накопичила вологу. Поточна щільність: {self._humidity_density:.2f} г/м³")
    
    def rain(self):
        if self.rain_probability > 70:
            self.humidity_density *= 0.5
            print(f"Йде дощ. Волога зменшилась до {self.humidity_density:.2f} г/м³")
            return True
        else:
            print(f"Дощу не буде. Поточна ймовірність: {self.rain_probability:.2f}%")
            return False
    
    def move(self, new_altitude):
        self._altitude = new_altitude
        print(f"Хмара перемістилась на висоту {self.altitude:.2f} км")
    
    def get_forecast(self):
        return (
            f" - Прогноз хмари:\n"
            f" - Площа: {self.area:.2f} км²\n"
            f" - Висота: {self.altitude:.2f} км\n"
            f" - Щільність вологи: {self.humidity_density:.2f} г/м³\n"
            f" - Ймовірність дощу: {self.rain_probability:.2f}%"
        )


class Aquarium:
    """
    Клас побутового об'єкта "Акваріум"
    Class for household object "Aquarium"
    
    Атрибути / Attributes:
    - length, width, height: розміри (10 < розмір < 200 см)
    - water_level: рівень води (0 <= water_level <= height)
    - fish_count: кількість риб (максимум 1 риба на 5 літрів води)
    - temperature: температура води (18 <= temperature <= 30 °C)
    - water_volume: об'єм води (обчислюється автоматично)
    """
    
    def __init__(self, length, width, height, water_level=0, fish_count=0, temperature=24):
        self._length = None
        self._width = None
        self._height = None
        self._water_level = 0
        self._fish_count = 0
        self._temperature = 24

        self.length = length
        self.width = width
        self.height = height
        self.water_level = water_level
        self.fish_count = fish_count
        self.temperature = temperature
        
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if not (10 < value < 200):
            raise ValueError("Довжина має бути від 10 до 200 см")
        self._length = value
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not (10 < value < 200):
            raise ValueError("Ширина має бути від 10 до 200 см")
        self._width = value
    
    
    @property
    def height(self):
        return self._height
  
    
    @height.setter
    def height(self, value):
        if not (10 < value < 200):
            raise ValueError("Висота має бути в межах (10, 200) см")
        self._height = value

    @property
    def water_level(self):
        return self._water_level
    
    @water_level.setter
    def water_level(self, value):
        if not (0 <= value <= self.height):
            raise ValueError("Рівень води має бути від 0 до висоти акваріума")
        self._water_level = value
    
    @property
    def fish_count(self):
        return self._fish_count
    
    @fish_count.setter
    def fish_count(self, value):
        if value < 0:
            raise ValueError("Кількість риб не може бути від'ємною")
        max_fish = self.water_volume / 5
        if value > max_fish:
            raise ValueError(f"Занадто багато риб. Максимум для поточного об'єму: {int(max_fish)}")
        self._fish_count = value
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if not (18 <= value <= 30):
            raise ValueError("Температура має бути в межах 18–30°C")
        self._temperature = value
    
    @property
    def water_volume(self):
        return (self.length * self.width * self.water_level) / 1000
    
    def add_water(self, level_increase):
        if level_increase < 0:
            raise ValueError("Збільшення рівня води не може бути від'ємним")
        new_level = self.water_level + level_increase
        if new_level > self.height:
            print("Заповнено до максимальної висоти")
        new_level = self.height
        self.water_level = new_level
        print(f"Додано воду. Поточний рівень: {self.water_level:.2f} см")
        max_fish = self.water_volume / 5
        if self.fish_count > max_fish:
            print(f"Kількість риб перевищує допустиму норму ({int(max_fish)} риб для об'єму {self.water_volume:.1f} л)")
    
    def add_fish(self):
        max_fish = self.water_volume / 5
        if self.fish_count + 1 <= max_fish:
            self.fish_count += 1
            print(f"Рибу додано. Тепер риби {self.fish_count}")
            return True
        else:
            print(f"Не можна додати рибу. Максимум для цього об'єму: {int(max_fish)}")
            return False
        """
        Метод: додати рибу / Method: add fish
        
        TODO:
        - Обчислити максимальну кількість риб для поточного об'єму
        - Перевірити чи можна додати ще одну рибу
        - Якщо можна: збільшити fish_count на 1
        - Вивести повідомлення про результат операції
        - Повернути True якщо риба додана, False якщо ні
        """
        pass
    
    def remove_fish(self):
        if self.fish_count > 0:
            self.fish_count -= 1
            print(f" Рибу забрали. Залишилось: {self.fish_count}")
            return True
        else:
            print("В акваріумі немає риб.")
            return False
    
    
    def heat(self, new_temperature):
        self.temperature = new_temperature
        print(f" Температура води встановлена на {self.temperature}°C")
        
    
    def inspect(self):
        max_fish = int(self.water_volume / 5)
        return (
            f" Інспекція акваріума:\n"
            f"Розміри: {self.length} x {self.width} x {self.height} см\n"
            f"Рівень води: {self.water_level} см\n"
            f" Об'єм води: {self.water_volume:.1f} л\n"
            f"Кількість риб: {self.fish_count} (максимум: {max_fish})\n"
            f"Температура: {self.temperature}°C"
        )


# Область для тестування / Testing area
if __name__ == "__main__":
    print("=== ТЕСТУВАННЯ ШАБЛОНІВ КЛАСІВ / TESTING CLASS TEMPLATES ===\n")
    
    # TODO: Розкоментуйте код нижче після реалізації класів
    # Uncomment code below after implementing classes
    
    
    # Тестування дерева / Testing tree
    print("1. ТЕСТУВАННЯ ДЕРЕВА / TESTING TREE")
    try:
        tree = Tree(10, 50)
        print(tree.get_info())
        tree.grow()
        tree.leaf_fall()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування чайника / Testing kettle
    print("2. ТЕСТУВАННЯ ЧАЙНИКА / TESTING KETTLE")
    try:
        kettle = Kettle(2.0)
        kettle.pour_water(1.5)
        print(kettle.get_status())
        kettle.turn_on()
        kettle.turn_off()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування хмари / Testing cloud
    print("3. ТЕСТУВАННЯ ХМАРИ / TESTING CLOUD")
    try:
        cloud = Cloud(100, 2.5, 15)
        print(cloud.get_forecast())
        cloud.accumulate_moisture(10)
        cloud.rain()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування акваріума / Testing aquarium
    print("4. ТЕСТУВАННЯ АКВАРІУМА / TESTING AQUARIUM")
    try:
        aquarium = Aquarium(50, 30, 40)
        aquarium.add_water(35)
        print(aquarium.inspect())
        aquarium.add_fish()
        aquarium.add_fish()
        aquarium.heat(26)
        print(aquarium.inspect())
    except Exception as e:
        print(f"Помилка: {e}")
        
   