"""
-------------------------------------------------------
Assignment 1, Task 9
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
# Imports
from functions import shift


fh_in = open('pelee.txt', 'r', encoding='utf-8')
fh_out = open('pelee_out.txt', 'w', encoding='utf-8')


fh_out.write(shift(fh_in.read(), 1))

estring = shift("David", 1)
print(estring)
