"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      16901XXXX
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-09"
-------------------------------------------------------
"""
# Imports


def duplicate_encode(word):
    """
        -------------------------------------------------------
        The goal of this exercise is to convert a string to a new string where
        each character in the new string is "(" if that character appears only
        once in the original string, or ")" if that character appears more than
        once in the original string. Ignore capitalization when determining if
        a character is a duplicate.
        Iterative
        Use: srt1 =duplicate_encode(word)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            str1 - string converted (string)
        -------------------------------------------------------
        Examples:
            "recede"   =>  "()()()"
        -------------------------------------------------------
        """
    word = word.lower()
    hset = {}
    for letter in word:
        if letter in hset:
            hset[letter] += 1
        else:
            hset[letter] = 1
    str1 = ''
    for each in word:
        if hset[each] == 1:
            str1 += '('
        else:
            str1 += ')'
    return str1


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    text = "recede"
    print(duplicate_encode(text))
