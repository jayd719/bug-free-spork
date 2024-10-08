"""
-------------------------------------------------------
Custom Function Library
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-26"
-------------------------------------------------------
"""
# Imports
from Letter import Letter
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    fh = file_variable.read().strip().upper()
    for each in fh:
        if each in ALPHA:
            bst.retrieve(Letter(each))

    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0

    for each in bst.preorder():
        total += each.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = 0
    for each in bst.preorder():
        total += each.count

    print('Letter Count/Percent Table')
    print('')
    print(f'Total Count: {total:,d}')
    print('')
    print('Letter  Count       %')
    print('---------------------')
    for each in bst.inorder():
        print(f'{each.letter:>6s} {each.count:>7,d}{(each.count/total):>6.2f}%')
    return
