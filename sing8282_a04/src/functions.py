"""
-------------------------------------------------------
Assignment 3 Custom Functions Library
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue


def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    ---------------------------------------------------------
    """
    target = Queue()
    # create a new queue instance

    while source1.is_empty() is False or source2.is_empty() is False:
        # repeat the process until both sources are empty
        if source1.is_empty() is False and source2.is_empty() is False:
            # if both source has elements in them
            target.insert(source1.remove())
            target.insert(source2.remove())

        else:
            # if either got empty before the other.
            if source1.is_empty() is False:
                target.insert(source1.remove())
            elif source2.is_empty() is False:
                target.insert(source2.remove())

    return target


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    while source.is_empty() is False:
        if source.peek() < key:
            target1.insert(source.remove())
        else:
            target2.insert(source.remove())
    return target1, target2
