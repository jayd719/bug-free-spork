"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts
from List_linked import List
from random import randint

SEP = '-' * 40

source = List()

i = 0
while i < 2:
    source.append(randint(0, 9))
    i += 1

print('TESTING RADIX SORT: LINKED LIST')
print(SEP)
print('Source Before Sort')
for val in source:
    print(val, end=',')
print('')
Sorts.radix_sort(source)
print(SEP)
print('Source After Sort')
for val in source:
    print(val, end=',')
print('')
