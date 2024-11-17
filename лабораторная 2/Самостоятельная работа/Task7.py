list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел
even_count = 0
odd_count = 0
# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных
for number in list_:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
# TODO вывести каких чисел больше
if even_count > odd_count:
    print("Четных чисел больше")
elif odd_count > even_count:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")