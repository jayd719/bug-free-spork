"""
-------------------------------------------------------
Assignment 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-26"
-------------------------------------------------------
"""
# Imports
from functions import do_comparisons
from functions import comparison_total
from functions import letter_table
from BST_linked import BST
from Letter import Letter

SEP = '-' * 40

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

fh = open('gibbon.txt', 'r', encoding='utf-8')
for each in DATA1:  # create BST 1
    bst1.insert(Letter(each))
do_comparisons(fh, bst1)
print(f'Comparing Order: {DATA1}')
print(f'Total Comparisons: {comparison_total(bst1):,d}')
print(SEP)
fh.close()


fh = open('gibbon.txt', 'r', encoding='utf-8')
for each in DATA2:  # create BST 2
    bst2.insert(Letter(each))
do_comparisons(fh, bst2)
print(f'Comparing Order: {DATA2}')
print(f'Total Comparisons: {comparison_total(bst2):,d}')
print(SEP)
fh.close()

fh = open('gibbon.txt', 'r', encoding='utf-8')
for each in DATA3:  # create BST 1
    bst3.insert(Letter(each))
do_comparisons(fh, bst3)
print(f'Comparing Order: {DATA3}')
print(f'Total Comparisons: {comparison_total(bst3):,d}')
print(SEP)
fh.close()
print(SEP)
print(SEP)
letter_table(bst1)
