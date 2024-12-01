# TODO решите задачу


import json

def task() -> float:
    json_file_path = 'input.json'
    total_sum = 0.0
    with open(json_file_path, 'r') as file:
        data = json.load(file)


    for item in data:
        if 'score' in item and 'weight' in item:
            product = item['score'] * item['weight']
            total_sum += product

    return round(total_sum, 3)


print(task())

