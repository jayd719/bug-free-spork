"""
-------------------------------------------------------
Custom Functions Library Lab 9
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
# Imports


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
     1652346    3 Dark City, 1998
     848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print('Hashes')
    print('Hash     Slot Key')
    print('-------- ---- --------------------')
    for movie in values:
        h = hash(movie)
        print(f'{h:>8d}{h%slots:>5d} {movie.title:3s},{movie.year}')
    return
