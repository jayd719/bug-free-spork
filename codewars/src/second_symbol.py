"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      16901XXXX
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-13"
-------------------------------------------------------
"""
# Imports


def second_symbol(s, symbol):
    """
        -------------------------------------------------------
       In this kata, you need to write a function that takes a string
       and a letter as input and then returns the index of the second
       occurrence of that letter in the string. If there is no such
       letter in the string, then the function should return -1. If
       the letter occurs only once in the string, then -1 should
       also be returned.
        Use: srt1 =second_symbol(s, symbol))
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            index - index of second occur in s
        -------------------------------------------------------
        Examples:
            "recede"   =>  "()()()"
        -------------------------------------------------------
        """
    index = [-1, -1]
    i = 0
    while index[1] == -1 and i < len(s):
        if s[i] == symbol:
            if index[0] == -1:
                index[0] = i
            else:
                index[1] = i
        i += 1
    return index[1]


def second_symbol_2(s, symbol):
    """
        -------------------------------------------------------
       In this kata, you need to write a function that takes a string
       and a letter as input and then returns the index of the second
       occurrence of that letter in the string. If there is no such
       letter in the string, then the function should return -1. If
       the letter occurs only once in the string, then -1 should
       also be returned.
        Use: srt1 =second_symbol(s, symbol))
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            index - index of second occur in s
        -------------------------------------------------------
        Examples:
            "recede"   =>  "()()()"
        -------------------------------------------------------
        """
    index = -1
    apear = 0
    i = 0
    while index == -1 and i < len(s):
        if s[i] == symbol:
            apear += 1
        if apear == 2:
            index = i
        i += 1
    return index


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    a = second_symbol('Hello world!!!', 'l')
    print(a)
