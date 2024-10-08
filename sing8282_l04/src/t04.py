"""
-------------------------------------------------------
Lab 4, Task 4
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
target.append(-3)
target.append(1)
target.append(2)
target.append(3)
target.append(4)
target.append(5)


for each in target:
    print(each)

print('')
n = target.index(2)
print(n)


print('')
value = target.find(2)
print(value)

b = 2 in target
print(b)

n = target.count(1)
print('')
print(n)

print('')
print(target.max())
print(target.min())

print(target[2])
