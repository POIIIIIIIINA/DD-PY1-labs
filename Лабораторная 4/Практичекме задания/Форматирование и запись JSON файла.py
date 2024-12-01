import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"

def task() -> None:
    ...  # TODO Десериализуйте содержимое файла из переменной INPUT_FILE
    with open(INPUT_FILE, encoding="utf-8") as f:
        json_data = json.load(f)
    ...  # TODO Сериализуйте содержимое в файл из переменной INPUT_FILE
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Нужно для проверки задания
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")