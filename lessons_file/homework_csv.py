import csv
from pathlib import Path


def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def write_csv(filepath: Path, content:list):
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file)
        writer.writerows(content)


if __name__ == "__main__":
    my_csv = Path(__file__).parent / "users_1.csv"
try:    
    content = read_file(my_csv)
    print(content, type(content))
except FileNotFoundError:
    print(f"Файл {my_csv} не знайдено.")    
    my_csv_2 = Path(__file__).parent / "new2.csv"   
    all_good = write_csv(my_csv_2, content)
    if all_good :
        print (f"файл{my_csv_2} записано")
    else:
        print(f"файл {my_csv_2} не вдалось записати")    


    