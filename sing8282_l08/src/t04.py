"""
-------------------------------------------------------
Lab 8, Task 4
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-16"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_code_bst
from morse import DATA1, DATA2, DATA3
from morse import decode_morse


VALUES = DATA3
bst = BST()
fill_code_bst(bst, VALUES)

print(len(bst))
for each in bst:
    print(each)
print("-" * 40)

result = decode_morse(bst, '... --- ...')
print(result)
