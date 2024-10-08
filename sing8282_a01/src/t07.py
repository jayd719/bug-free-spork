"""
-------------------------------------------------------
Assignment 1, Task 7
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
# Imports
from functions import matrixes_multiply


a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
c = matrixes_multiply(a, b)
print(c)

print('----------------')


a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8], [9, 10], [11, 12]]
c = matrixes_multiply(a, b)
print(c)
