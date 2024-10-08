"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      16901XXXX
Email:   sing8282@mylaurier.ca
__updated__ = "2023-06-23"
-------------------------------------------------------
"""
# Imports


def long_string(text):
    ls = len(text)
    if ls > 10:
        text = f'{text[0]}{ls-2}{text[ls-1]}'
    return text


n = int(input())
while n > 0:
    word = input()
    s = long_string(word)
    n -= 1

    print(s)
