"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_combine

source1 = Queue()
source2 = Queue()

# insert elements in source 1
source1.insert(5)
source1.insert(8)
source1.insert(12)
source1.insert(8)
source1.insert(15)
source1.insert(16)
source1.insert(17)


# insert elements in source 2
source2.insert(7)
source2.insert(9)
source2.insert(14)
source2.insert(18)
source2.insert(19)


target = queue_combine(source1, source2)


# Output
print('Source 1:')  # print source 1
for v in source1:
    print(v)
print('-' * 10)

print('Source 2:')  # print source 2
for k in source2:
    print(k)
print('-' * 10)

print('Target')  # print target
for m in target:
    print(m)
print('-' * 10)
