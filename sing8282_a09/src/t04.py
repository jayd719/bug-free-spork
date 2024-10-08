"""
-------------------------------------------------------
Assignment 8, Task 4
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

SEP = '-' * 40
VALUES = [11, 7, 15, 6, 9, 12, 18, 8]

bst = BST()

for val in VALUES:
    bst.insert(val)

print(bst.node_counts())

print(1 in bst)

print(bst.parent(8))
print(bst.parent_r(8))
