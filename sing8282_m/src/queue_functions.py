"""
-------------------------------------------------------
Midterm Queue Functions
-------------------------------------------------------
Author: Jd Singh
ID:     169018282
Email:  sing8282@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""


def queue_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of values in source. When finished, values
    in source are rotated n positions to the right.
    Use: queue_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the Queue to rotate (Queue)
        n - amount to rotate Queue values (int)
    Returns‌​‌​​​​‌​​‌‌​​​​​​‌‌‌​‌​‌​‌​:
        None
    -------------------------------------------------------
    """
    i = 0
    if n >= 0:
        while i < n:
            a = source.remove()
            source.insert(a)
            i += 1
    else:
        j = len(source) + n
        while i < j:
            a = source.remove()
            source.insert(a)
            i += 1
    return
