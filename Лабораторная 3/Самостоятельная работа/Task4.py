# TODO реализовать функцию
def get_sentences_list(str_words):
    sentences_list = []
    for sentence in str_words.split("."):
        if sentence:
            sentences_list.append(sentence.strip())

    return sentences_list
print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
