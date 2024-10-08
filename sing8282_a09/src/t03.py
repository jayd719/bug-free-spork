"""
-------------------------------------------------------
Assignment 8, Task 3
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
# Imports
from functions import insert_words
from functions import comparison_total
from Hash_Set_BST import Hash_Set

fh = open('gibbon.txt', 'r', encoding='utf-8-sig')
# open the file to be read

hash_set = Hash_Set(20)
# create instance of hast set


insert_words(fh, hash_set)

total, max_word = comparison_total(hash_set)


# output
print(f'Total Comparisons: {total:,d}')
print(
    f"Word with maximum comparisons '{max_word.word}':{max_word.comparisons}")
