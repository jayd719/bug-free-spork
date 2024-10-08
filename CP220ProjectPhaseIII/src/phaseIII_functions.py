"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-11-28"
-------------------------------------------------------
"""
# Imports

# Constants


def reverseArray(a):
    i = 0
    n = len(a) - 1

    while i <= n:
        front = a[i]
        rear = a[n]

        a[n] = front
        a[i] = rear
        i += 1
        n = n - 1

    return a


print(reverseArray([1, 2, 3, 4]))
