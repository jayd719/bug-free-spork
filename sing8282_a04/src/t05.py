"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

# insert values in in priority queue
pq.insert(1)
pq.insert(2)
pq.insert(3)
pq.insert(4)

target1, target2 = pq_split_key(pq, 3)


# Output

print('Source:')
for each in pq:
    print(each)
print('-' * 10)
print('-' * 10)
print('Target1:')
for each in target1:
    print(each)
print('-' * 10)
print('Target2:')
for each in target2:
    print(each)
print('-' * 10)
