"""
-------------------------------------------------------
Lab 4, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from List_array import List


target = List()
target.append(1)
target.append(2)
target.append(3)
target.append(4)


for each in target:
    print(each)

# target.insert(32, 'as')

print('')
for each in target:
    print(each)

print('')

target.remove(2)
for each in target:
    print(each)
