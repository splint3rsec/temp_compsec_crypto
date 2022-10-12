"""
week2 task for computer security practice course.

"""

# Variables
TABLE = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,\
        'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,\
        'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,\
        'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,\
        'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29,\
        'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35,\
        'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41,\
        'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47,\
        'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53,\
        '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59,\
        '8': 60, '9': 61, '+': 62, '/': 63}

# First function
def hex2bin(c:str) -> str:
    """
    hexadecimal to binary function.
    >>> hex2bin('f')
    '1111'
    >>> hex2bin('5')
    '101'
    >>> hex2bin('1')
    '1'
    """
    c = str(c)
    to_hex = int(c, 16)
    to_bin = bin(to_hex)
    return to_bin[2:]

# # Second function
def bin2hex(c:str) -> str:
    """
    >>> bin2hex('1111')
    'f'
    >>> bin2hex('100001')
    '21'
    >>> bin2hex('1')
    '1'
    """
    to_bin = int(c, 2)
    to_hex = hex(to_bin)
    return to_hex[2:]

# # Third function
def fillupbyte(c:str) -> str:
    """
    >>> fillupbyte('011')
    '00000011'
    >>> fillupbyte('1')
    '00000001'
    >>> fillupbyte('10111')
    '00010111'
    >>> fillupbyte('11100111')
    '11100111'
    >>> fillupbyte('111001111')
    '0000000111001111'
    """
    while len(c) % 8 != 0:
        c = '0' + c
    return c

# Fourth function
def int2base64(i:int) -> str:
    """
    >>> int2base64(0x61)
    'YQ=='
    >>> int2base64(0x78)
    'eA=='
    """
    ctr, result = 0, ''
    binary = fillupbyte(bin(i)[2:])
    L = [binary[k:k+6] for k in range(0, len(binary), 6)]
    for k in L:
        while len(k) % 6 != 0:
            k += '0'
        L[ctr] = k
        ctr += 1
    ctr = 0
    L = [int(k, 2) for k in L]
    for index in L:
        for key, value in TABLE.items():
            if index == value:
                L[ctr] = key
        result += L[ctr]
        ctr += 1
    while len(result) % 4 != 0:
        result += '='
    return result

# Fifth function
def hex2base64(i:str) -> str:
    """
    >>> hex2base64('61')
    'YQ=='
    >>> hex2base64('123456789abcde')
    'EjRWeJq83g=='
    """
    ctr, result = 0, ''
    binary = fillupbyte(hex2bin(i))
    L = [binary[k:k+6] for k in range(0, len(binary), 6)]
    for k in L:
        while len(k) % 6 != 0:
            k += '0'
        L[ctr] = k
        ctr += 1
    ctr = 0
    L = [int(k, 2) for k in L]
    for index in L:
        for key, value in TABLE.items():
            if index == value:
                L[ctr] = key
        result += L[ctr]
        ctr += 1
    while len(result) % 4 != 0:
        result += '='
    return result


# Main
if __name__ == '__main__':
    import doctest
    doctest.testmod()