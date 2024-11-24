# TODO Напишите функцию print_stairs
# TODO вызвать функцию без аргументов и с аргументом равным 10
def print_stairs(count_stairs=4):
    for i in range(1, count_stairs + 1):
        print("*" * i)
print_stairs()
print_stairs(10)
