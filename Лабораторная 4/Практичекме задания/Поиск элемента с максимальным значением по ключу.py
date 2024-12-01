import json


FILENAME = "input.json"


def task() -> dict:
    ...  # TODO считать содержимое JSON файла
    with open(FILENAME) as f:
        json_data = json.load(f)
    ...  # TODO найти максимальный элемент по ключу score
    return max(json_data, key=lambda item: item["score"])
if __name__ == '__main__':
    print(task())
