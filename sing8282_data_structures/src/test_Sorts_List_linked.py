"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-30"
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    values = List()
    i = 0
    while i < SIZE:
        values.append(Number(i))
        i += 1
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    values = List()
    i = SIZE - 1
    while i != -1:
        values.append(Number(i))
        i -= 1

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    lists = List()
    for i in range(TESTS):
        row_list = List()
        for j in range(SIZE):
            row_list.append(Number(random.randint(0, XRANGE)))
        lists.append(row_list)
    return lists

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    values_reversed = create_reversed()
    values_sorted = create_sorted()
    values_random = create_randoms()

    Number.comparisons = 0
    Sorts.swaps = 0
    func(values_sorted)
    comparisons_in_order = Number.comparisons
    sorts_in_order = round(Sorts.swaps)

    Number.comparisons = 0
    Sorts.swaps = 0
    func(values_reversed)
    comparisons_reverse = Number.comparisons
    sorts_reverse = round(Sorts.swaps)

    Number.comparisons = 0
    Sorts.swaps = 0
    for val in values_random:
        func(val)
    comparisons_random = Number.comparisons // len(values_random)
    swaps_random = round(Sorts.swaps) // len(values_random)
    print(f'{title:14} {comparisons_in_order:8} {comparisons_reverse:8} {comparisons_random:8} {sorts_in_order:8} {sorts_reverse:8}{swaps_random:8}')

    return
