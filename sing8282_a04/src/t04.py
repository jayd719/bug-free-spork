"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue


source1 = Queue()
source2 = Queue()
target = Queue()

# insert elements in source 1
source1.insert("Adam")
source1.insert("Eve")
source1.insert("Movie")
source1.insert('Barber')
source1.insert('Car')

# insert elements in source 2
source2.insert('Pizza')
source2.insert('Burger')
source2.insert('Gear')


target.combine(source1, source2)

# Output
print('Source 1:')  # print source 1
for v in source1:
    print(v)
print('-' * 10)

print('Source 2:')  # print source 2
for k in source2:
    print(k)
print('-' * 10)

print('Target:')  # print target
for m in target:
    print(m)
print('-' * 10)
