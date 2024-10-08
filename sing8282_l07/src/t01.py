"""
-------------------------------------------------------
Lab 7, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-16"
-------------------------------------------------------
"""
# Imports
from List_linked import List
lst = List()
target = List()


source = [22, 33, 11, 55, 44]
source2 = ['ADAM', 'SMITH', 'WORK', 'CPI']
source3 = ['ADAM', 'SMITH', 'WORK', 'CPI']
for val in source2:
    lst.append(val)


for val in source3:
    target.append(val)

target.remove('ADAM')


b = lst.identical_r(target)
print(b)

even, odd = lst.split_alt_r()

print('----------------')
print('Even')
for each in even:
    print(even)
print('ODD')
for each in odd:
    print(each)
