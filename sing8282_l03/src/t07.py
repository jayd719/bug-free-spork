"""
-------------------------------------------------------
Lab 3, Task 8
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports

from utilities import array_to_pq, pq_to_array
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

source = ['Trees', 'Cats', 'Dogs', 'Ice Cream']

#source = [1, 2, 3, 4]

array_to_pq(pq, source)

for each in pq:
    print(each)


print('-' * 40)

target = []
pq_to_array(pq, target)

print(target)
