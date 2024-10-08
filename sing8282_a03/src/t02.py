"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack


items = [8, 14, 12, 9, 8, 7, 5]
items.reverse()
source = Stack()
for item in items:
    source.push(item)

print('source:')
for values in source:
    print(values)
print('-' * 40, '\n')

target1, target2 = source.split_alt()

print('target 1')
for m in target1:
    print(m)
print('-' * 40, '\n')
print('target 2')
for k in target2:
    print(k)
