"""
-------------------------------------------------------
Assignment 10, Task 4
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""
# Imports

# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque
from random import randint

SEP = '-' * 40

source = Deque()

i = 0
while i < 5:
    source.insert_rear(randint(0, 9))
    i += 1

print('TESTING GNOME SORT: DEQUE LINKED')
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
