def get_list_number_divisors(number):
    ...  # TODO Найдите список делителей числа number
    if number < 1:
        raise ValueError("Число должно быть натуральным (больше нуля).")
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors
print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
