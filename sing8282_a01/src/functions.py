"""
-------------------------------------------------------
Custom Functions Library
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
# Imports

# Constants
ALPHA = 'abcdefghijkmnopqrstuvwxyz'
SPECAIL_CHAR = '\?><{}[]+-=()*&^%$#@!;:"|/ .'
VOWELS = 'AEIOU'

C1 = 'way'
C2 = 'ay'


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    clean_list = []
    for i in values:
        if i not in clean_list:
            clean_list.append(i)
    values = clean_list
    return None


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u, l, d, w, r = 0, 0, 0, 0, 0
    content = fv.read()
    for char in content:
        if char in ALPHA.upper():
            u += 1
        elif char in ALPHA:
            l += 1
        elif char == ' ':
            w += 1
        elif char.isdigit():
            d += 1
        else:
            r += 1
    return u, l, d, w, r


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:s
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    if sub in string:
        i = 0
        while i < len(string):
            if string[i:(i + len(sub))] == sub:
                locations.append(i)
            i += 1
    return locations


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    if (year % 4) == 0:
        leap_year = True
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap_year = True
            else:
                leap_year = False
    return leap_year


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = False
    if name[0].isdigit() is False:
        for char in name:
            if char in SPECAIL_CHAR:
                valid = False
                break
            valid = True

    return valid


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    col = 0

    j = 0
    transpose_able = True
    while j + 1 < len(a):
        if len(a[j]) != len(a[j + 1]):
            transpose_able = False
        j += 1

    if transpose_able:
        while col < len(a[0]):
            row, c = 0, []
            while row < len(a):
                c.append(a[row][col])
                row += 1
            col += 1
            b.append(c)
    return b


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []
    for i in range(len(a)):
        d = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(a[0])):
                s += (a[i][k] * b[k][j])
            d.append(s)
        c.append(d)
    return c


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ''

    if word[0].upper() in VOWELS:
        pl = f'{word}{C1}'

    else:
        pl = f'{word[1:]}{word[:1]}{C2}'

    if word[0]in ALPHA.upper():
        pl = f'{pl[:1].upper()}{pl[1:].lower()}'
    return pl


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ''
    for char in string.lower():
        if char in ALPHA:
            i = 0
            while i < len(ALPHA):
                if char == ALPHA[i]:
                    estring += ALPHA[i + n]
                i += 1
        else:
            estring += char

    return estring.upper()
