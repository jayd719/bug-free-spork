"""
-------------------------------------------------------
Lab 4, Task 6
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list
from utilities import list_to_array
from List_array import List


target = List()
source = [1, 2, 3, 4, 5]
array_to_list(target, source)

for e in target:
    print(e)

print('')
print(source)


list_to_array(target, source)
print('_____________________')
for e in target:
    print(e)

print(source)
