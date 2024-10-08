"""
-------------------------------------------------------
Asignment 6, Task 2
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

SEP = "-" * 60
VALUES = [4, 3, 5, 1, 2, 0, 3]
VALUES2 = [4, 3, 5, 1, 2]
VALUES3 = [10, 11, 12, 13]
# VALUES = [10]


def test_is_empty():
    print()
    print(SEP)
    print("Queue: Test Empty")
    source = Priority_Queue()
    for v in source:
        print(v)
    print(f"source.is_empty(): {source.is_empty()}")


def test_len():
    print()
    print(SEP)
    print("Queue: Len")
    source = Priority_Queue()
    for v in source:
        print(v)
    print(f"len(source): {len(source)}")


def test_insert():
    print()
    print(SEP)
    print("Queue: Insert")
    source = Priority_Queue()
    for value in VALUES:
        source.insert(value)

    for v in source:
        print(v)
    print(f"len(source): {len(source)}")
    print()
    print(SEP)
    print('TEST Remove')
    print(f'Removed: {source.remove()}')
    print('After Remove')
    for v in source:
        print(v)
    print(f'PEEK: {source.peek()}')

    print()
    print(SEP)
    print('TEST Remove')
    print(f'Removed: {source.remove()}')
    print('After Remove')
    for v in source:
        print(v)
    print(f'PEEK: {source.peek()}')


def test_move():
    print()
    print(SEP)
    print("Queue: Test Move Front To Rear")
    target = Priority_Queue()
    source = Priority_Queue()
    for val in VALUES:
        target.insert(val)
    print('Initial Target')
    for v in target:
        print(v)
    for val in VALUES2:
        source.insert(val)
    print('Initial Source')
    for v in source:
        print(v)
    print(SEP)
    print('After Move Operation')
    target._move_front_to_rear(source)
    print('Updated Target')
    for v in target:
        print(v)
    print('Updated Source')
    for v in source:
        print(v)
    print('-')


def test_append():
    print()
    print(SEP)
    print("Queue: Test Append")
    target = Priority_Queue()
    source = Priority_Queue()
    for val in VALUES:
        target.insert(val)
    print('Initial Target')
    for v in target:
        print(v)
    for val in VALUES2:
        source.insert(val)
    print('Initial Source')
    for v in source:
        print(v)
    print(SEP)
    print('After Append')
    target._append_queue(source)
    print('Updated Target')
    for v in target:
        print(v)
    print('Updated Source')
    for v in source:
        print(v)


def test_split_alt():
    print()
    print(SEP)
    print("Queue: Test Split_alt")
    source = Priority_Queue()
    for val in VALUES:
        source.insert(val)
    print('Initial Source')
    for v in source:
        print(v)
    target1, target2 = source.split_alt()
    print('Target 1')
    for val in target1:
        print(val)
    print(SEP)
    print('Target 2')
    for val in target2:
        print(val)

    print()
    print(f'Source Empty: {source.is_empty()}')


def test_split_key():
    print()
    print(SEP)
    print("Queue: Test Split_alt")
    source = Priority_Queue()
    for val in VALUES:
        source.insert(val)
    print('Initial Source')
    for v in source:
        print(v)
    target1, target2 = source.split_key(3)
    print('Target 1')
    for val in target1:
        print(val)
    print(SEP)
    print('Target 2')
    for val in target2:
        print(val)

    print()
    print(f'Source Empty: {source.is_empty()}')


def test_combine():
    print()
    print(SEP)
    print("Queue: Test COMBINE")
    target = Priority_Queue()
    source1 = Priority_Queue()
    source2 = Priority_Queue()
    for val in VALUES:
        source1.insert(val)
    print('Initial Source1')
    for v in source1:
        print(v)
    for val in VALUES2:
        source2.insert(val)
    print('Initial Source2')
    for v in source2:
        print(v)
    print(SEP)
    target.combine(source1, source2)
    for v in target:
        print(v)
    print()
    print(f'Source 1 is Empty:{source1.is_empty()}')
    print(f'Source 2 is Empty: {source2.is_empty()}')


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Test Queue")
    test_is_empty()
    test_len()
    test_insert()
    test_move()
    test_append()
    test_split_alt()
    test_split_key()
    test_combine()
