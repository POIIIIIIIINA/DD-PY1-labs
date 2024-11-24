# TODO Напишите функцию `is_palindrome`
def is_palindrome(str_):
    str_clear = ''.join(str_.lower().split())
    return str_clear == str_clear[::-1]