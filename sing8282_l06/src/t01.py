"""
-------------------------------------------------------
Lab 6, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst = List()

print(lst.is_empty())

source = [1, 3, 4, 5, 1]
for val in source:
    lst.append(val)

print(lst.is_empty())

lst.prepend(7)
lst.append(1)

# lst.insert(2, 99)
lst.remove(7)
lst.remove(7)
lst.prepend(7)
lst.__setitem__(3, 10)
print('')
print('List')
for each in lst:
    print(f'{each:>4d}')

print('-' * 40)
print('Linear Search')
print(lst.count(1))

print(lst.max())
print(lst.min())
print(lst.peek())

print('---')
print(lst[-2])
