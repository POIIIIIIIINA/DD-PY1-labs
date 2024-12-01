INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO перезаписать содержимое одного файла в другой
    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            for line in input_file:
                output_file.write(line.upper())


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
