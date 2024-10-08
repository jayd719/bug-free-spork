"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      16901XXXX
Email:   sing8282@mylaurier.ca
__updated__ = "2023-07-29"
-------------------------------------------------------
"""
# Imports

# TODO: NOTES

"""
Recursion 

1. call stack problem
2. slowness of CPU due multi head
3. call stack overflow 



"""


def reverse_string(string):
    str1 = ''
    if len(string):
        str1 = string[-1] + reverse_string(string[:-1])
    return str1


def check_palindrome(string):
    palindrome = True
    if len(string) > 1:
        if string[0] == string[-1]:
            palindrome = check_palindrome(string[1:-1])
        else:
            palindrome = False
    return palindrome


def convert_to_binary(number, result):
    if number > 0:
        result = convert_to_binary(number // 2, str(number % 2)) + result
    return result


def sum_of_numbers(n):
    sum_ = 0
    if n != 0:
        sum_ += n + sum_of_numbers(n - 1)
    return sum_


def binary_sreach(string, s):
    if len(string):
        pass
    else:
        contains = False

    return contains

# print(reverse_string('this'))
# print(check_palindrome('kaak'))
# print(convert_to_binary(233, ''))


print(sum_of_numbers(3))
