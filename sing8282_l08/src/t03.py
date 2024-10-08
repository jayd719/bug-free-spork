"""
-------------------------------------------------------
Lab 8, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-16"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_letter_bst
from morse import DATA1, DATA2, DATA3
from morse import encode_morse


VALUES = DATA2
bst = BST()
fill_letter_bst(bst, VALUES)

print(len(bst))
for each in bst:
    print(each)
print("-" * 40)

result = encode_morse(bst, 'My name is David Brown.')
print(result)
