"""
-------------------------------------------------------
Assignment 8, Task 1
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
# Imports

from BST_linked import BST

SEP = '-' * 40
VALUES = [3, 1, 5, 0, 2, 4, 6]
VALUES = [11, 7, 15, 6, 9, 12, 18, 13, 16]


# VALUES2 = []
# VALUES = [11, 22, 33, 44]
VALUES2 = []


def test_equal():
    print(SEP)
    print('Test Equal')
    bst1 = BST()
    bst2 = BST()
    for val in VALUES:
        bst1.insert(val)

    for val in VALUES:
        bst2.insert(val)

    print(f'BST1 == BST2: {bst1==bst2}')


def test_is_balanced():
    print(SEP)
    print('Test Is Balanced')
    bst = BST()
    for val in VALUES:
        bst.insert(val)
    print(f'BST BALANCED: {bst.is_balanced()}')


def test_is_valid():
    print(SEP)
    print('TEST IS VALID')
    bst = BST()
    for val in VALUES:
        bst.insert(val)
    print(f'BST IS VALID: {bst.is_valid()}')


def test_min():
    print(SEP)
    print('TEST MIN')
    bst = BST()
    for val in VALUES:
        bst.insert(val)
    print(f'MIN: {bst.min()}')


def test_leaf_count():
    print(SEP)
    print('TEST COUNT')
    bst = BST()
    for val in VALUES:
        bst.insert(val)
    print(f'Leaf Count: {bst.leaf_count()}')


def test_one_child_count():
    print(SEP)
    print('Test One Child Count')
    bst = BST()
    for val in VALUES:
        bst.insert(val)
    print(f'One Child Count: {bst.one_child_count()}')
    print(f'Two Child Count: {bst.two_child_count()}')
    print(SEP)
    print(f'IN ORDER: {bst.inorder()}')
    print(f'PRE ORDER: {bst.preorder()}')
    print(f'Post ORDER: {bst.postorder()}')
    print(f'Level ORDER: {bst.levelorder()}')


if __name__ == "__main__":
    print('TESTING BST')
    test_equal()
    test_is_balanced()
    test_is_valid()
    test_min()
    test_leaf_count()
    test_one_child_count()
