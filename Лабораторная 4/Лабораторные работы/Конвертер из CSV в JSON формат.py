# TODO импортировать необходимые молули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [OrderedDict(row) for row in reader]
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
