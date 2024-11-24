# TODO реализовать функцию
def get_unique_words(str_words):
        unique_words = list(set(str_words.split()))
        unique_words.sort()
        return unique_words
print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))


