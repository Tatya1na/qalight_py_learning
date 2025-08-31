import json
from pathlib import Path


def read_json(filepath: Path) -> dict:
    """
    Читає JSON файл та повертає його вміст як Python об'єкт.
    
    Args:
        filepath (Path): Шлях до JSON файла
        
    Returns:
        dict/list: Вміст JSON файла
        
    Raises:
        FileNotFoundError: Якщо файл не знайдено
        json.JSONDecodeError: Якщо файл містить невалідний JSON
    """

    with open(filepath, "r", encoding="utf-8") as file:
        content = json.load(file)
        return content

def write_json(filepath: Path, content:dict):
    """
    Записує Python об'єкт у JSON файл.
    
    Args:
        data (dict/list): Дані для запису
        filepath (Path): Шлях до файла для запису
        
    Returns:
        bool: True якщо успішно записано, False в іншому випадку
    """
    try:    
     with open(filepath, "w", encoding="utf-8", ) as file:
        json.dump(content, file, indent=4)
        return True
    except:
        (OSError, TypeError)
        return False

if __name__ == "__main__":
    my_json = Path(__file__).parent / "test_result.json"
    content = read_json(my_json)
    print(content, type(content))
    json_string = '{"name": "Ivan", "age": 25, "city": "Kyiv", "pass": 95, "skip": 5,  "failed": 0, "is_failed": true}'
    json_to = json.loads(json_string)
    print(json_to)
    new_json = Path(__file__).parent / "new.json"
    write_json(new_json, json_to)