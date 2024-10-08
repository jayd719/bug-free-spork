"""
-------------------------------------------------------
Assignment 10, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""
# Imports

# Imports
from Sorts_array import Sorts
from List_array import List
from random import randint

SEP = '-' * 40

source = List()

i = 0
while i < 6:
    source.append(randint(0, 9))
    i += 1

print('TESTING GNOME SORT: ARRAY LIST')
print(SEP)
print('Source Before Sort')
for val in source:
    print(val, end=',')
print('')

Sorts.gnome_sort(source)
print(SEP)
print('Source After Sort')
for val in source:
    print(val, end=',')
print('')
