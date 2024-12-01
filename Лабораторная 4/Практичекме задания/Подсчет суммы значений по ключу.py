import json


FILENAME = "input.json"


def task() -> int:
    ...  # TODO Десериализуйте содержимое JSON файла
    with open(FILENAME) as f:
        json_data = json.load(f)
    ...  # TODO Просуммируйте все значения по ключу contains_improvement_appeals
    list_values = [item["contains_improvement_appeals"] for item in json_data]
    return sum(list_values)

if __name__ == '__main__':
    print(task())
