"""
week3 task for computer security practice course.

"""
import doctest
from operator import itemgetter

# First function
def hex2string(data:str) -> str:
    """
    >>> hex2string('61')
    'a'
    >>> hex2string('776f726c64')
    'world'
    >>> hex2string('68656c6c6f')
    'hello'
    """
    result = ''.join([chr(int(bin(int(data[x:x+2], 16))[2:], 2)) for x in range(0, len(data), 2)])
    return result

# Second function
def string2hex(data:str) -> str:
    """
    >>> string2hex('a')
    '61'
    >>> string2hex('hello')
    '68656c6c6f'
    >>> string2hex('world')
    '776f726c64'
    >>> string2hex('foo')
    '666f6f'
    """
    l = ''.join([hex(ord(x))[2:] for x in data])
    return l

# Third function
def hex_xor(data1:str, data2:str) -> str:
    """
    >>> hex_xor('0aabbf11','12345678')
    '189fe969'
    >>> hex_xor('12cc','12cc')
    '0000'
    >>> hex_xor('1234','2345')
    '3171'
    >>> hex_xor('111','248')
    '359'
    >>> hex_xor('8888888','1234567')
    '9abcdef'
    """
    result = ''.join([hex(t)[2:] for t in [((int(x, 16))^(int(y, 16))) for x,y in zip(data1, data2)]])
    return result

# Fourth function
def encrypt_single_byte_xor(msg:str, key:str) -> str:
    """
    >>> encrypt_single_byte_xor('aaabbccc','00')
    'aaabbccc'
    >>> encrypt_single_byte_xor(string2hex('hello'),'aa')
    'c2cfc6c6c5'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa'))
    'hello'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa'))
    'Encrypt and decrypt are the same'
    """
    int_key = int(key, 16)
    divided_message = [msg[x:x+2] for x in range(0,len(msg),2)]
    xored_list = [int(x, 16) ^ int_key for x in divided_message]
    result = ''.join([hex(t)[2:] for t in xored_list])
    return result

# Fifth function
def decrypt_single_byte_xor(cipher:str) -> str:
    """
    >>> decrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480')
    'Hi! You have found me!'
    >>> decrypt_single_byte_xor('b29e9f96839085849d9085989e9f82d1889e84d199908794d197989f95d1859994d181908282869e8395d0')
    'Congratulations you have find the password!'
    """
    character_freq = {
        'e':0.1260,'t':0.0937,'a':0.0834,'o':0.0770,'n':0.0680,'i':0.0671,'h':0.0611,'s':0.0611,\
        'r':0.0568,'l':0.0424,'d':0.0414,'u':0.0285,'c':0.0273,'m':0.0253,'w':0.0234,'y':0.0204,\
        'f':0.0203,'g':0.0192,'p':0.0166,'b':0.0154,'v':0.0106,'k':0.0087,'j':0.0023,'x':0.0020,\
        'q':0.0009,'z':0.0006
    }
    possible_keys = [hex(x)[2:] for x in range(0,pow(2, 8))]
    could_be, values = [], []
    for item in possible_keys:
        i = possible_keys.index(item)
        if len(item) != 2:
            possible_keys[i] = '0' + possible_keys[i]

    for key in possible_keys:
        could_be.append(hex2string(encrypt_single_byte_xor(cipher, key)))

    for possible in could_be:
        a = sum([character_freq.get(chr(byte), 0) for byte in bytes(possible.lower(), 'utf-8')])
        values.append([possible, a])

    result = sorted(values, key=itemgetter(1), reverse=True)

    return result[0][0]

# Main
if __name__ == "__main__":
    doctest.testmod()
