"""
-------------------------------------------------------
Custom Function Library- Assignment 9
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
# Imports
from Word import Word
# constants
ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    fd = fv.read().split(' ')

    for word in fd:
        if len(word):
            i, add = len(word) - 1, True
            while i > -1 and add:
                # to save time, checking the work backwards
                if word[i].lower() not in ALPHA:
                    add = False
                i -= 1
            if add is True and word != ' ':
                hash_set.insert(Word(word.lower()))
    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = None
    max_comparisons = 0

    for val in hash_set:
        if val.comparisons > max_comparisons:
            max_comparisons = val.comparisons
            max_word = val
        total += val.comparisons
    return total, max_word
