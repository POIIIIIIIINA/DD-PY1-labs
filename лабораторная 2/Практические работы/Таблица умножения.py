# TODO Распечатать таблицу умножения
for i in range(2,10):
    for y in range(2,10):
        if y is 9 :
            print(f'{i * y:2}')
        else:
            print(f'{i*y:2}',end=" ")