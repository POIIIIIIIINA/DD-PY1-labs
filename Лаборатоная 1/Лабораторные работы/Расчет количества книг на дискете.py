# TODO Найдите количество книг, которое можно разместить на дискете

weight_book = 25*50*100*4
weight_mb = 1.44*1024*1024
amount_book = round(weight_mb//weight_book)
print("Количество книг, помещающихся на дискету:", amount_book)
