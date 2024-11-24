# TODO Напишите функцию find_common_items
def find_common_items(last_week_purchases, current_week_purchases):
    common_purchases = list(set(last_week_purchases).intersection(current_week_purchases))
    common_purchases.sort()
    return common_purchases
last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
