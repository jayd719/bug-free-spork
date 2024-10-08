"""
-------------------------------------------------------
Task 1-Camel Case Conversion
-------------------------------------------------------
Author:  JD
ID:      16901XXXX
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-09"
-------------------------------------------------------
"""


def to_camel_case_r(text, str1='', cap=False):
    """
        -------------------------------------------------------
        Complete the method/function so that it converts dash/underscore
        delimited words into camel casing. The first word within the output
        should be capitalized only if the original word was capitalized
        (known as Upper Camel Case, also often referred to as Pascal case).
        The next words should be always capitalized.
        recursive
        Use: srt1 =to_camel_case_r(text)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            str1 - string converted to camel case(string)
        -------------------------------------------------------
        Examples:
            "the-stealth-warrior" gets converted to "theStealthWarrior"
        -------------------------------------------------------
        """
    if len(text):
        if text[0] == '-' or text[0] == "_":
            str1 += to_camel_case_r(text[1:], str1, True)
        elif cap is True:
            str1 += f'{text[0].upper()}' + \
                to_camel_case_r(text[1:], str1, False)
        else:
            str1 += f'{text[0]}' + to_camel_case_r(text[1:], str1, False)
    return str1


def to_camel_case(text):
    """
        -------------------------------------------------------
        Complete the method/function so that it converts dash/underscore
        delimited words into camel casing. The first word within the output
        should be capitalized only if the original word was capitalized
        (known as Upper Camel Case, also often referred to as Pascal case).
        The next words should be always capitalized.
        Iterative
        Use: srt1 =to_camel_case_r(text)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
            str1 - string converted to camel case(string)
        -------------------------------------------------------
        Examples:
            "the-stealth-warrior" gets converted to "theStealthWarrior"
        -------------------------------------------------------
        """
    i = 0
    skip_index = []
    cap_index = []
    while i < len(text):
        if text[i] == '_' or text[i] == '-':
            skip_index.append(i)
            cap_index.append(i + 1)
        i += 1
    i = 0
    str1 = ''
    while i < len(text):
        if i not in skip_index:
            if i in cap_index:
                str1 += text[i].upper()
            else:
                str1 += text[i]
        i += 1
    return str1


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    text = "mid_te-rm-tes_ting"
    print(to_camel_case_r(text))
    print(to_camel_case(text))
