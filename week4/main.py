"""
week4 task for computer security practice course.

"""
import doctest
from turtle import pos

# Aux function
def decompose(msg:str) -> list:
    """
    Auxiliary function to decompose a message to a list of separated chars.
    """
    return ([msg[c:c+1] for c in range(0, len(msg), 1)])

# First task
def encrypt_by_add_mod(msg:str, key:int) -> str:
    """
    >>> encrypt_by_add_mod('Hello',123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    """
    result=[]
    sub_message = decompose(msg)
    for char in sub_message:
        result.append((ord(char) + key) % 256)
        final = "".join([chr(c) for c in result])
    return final

# Second task
def encrypt_xor_with_changing_key_by_prev_cipher(msg:str, key:int, method:str) -> str:
    """
    >>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
    '3V:V9'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    """
    cipher, plain = [], []
    sub_message = decompose(msg)
    if method == "encrypt":
        # Encryption
        ctr = 1
        c1 = ord(sub_message[0]) ^ key
        cipher.append(c1)
        for m in sub_message[1:]:
            cipher.append(ord(m) ^ cipher[ctr-1])
            ctr += 1
        final_cipher = "".join([chr(c) for c in cipher])
        return final_cipher
    elif method == "decrypt":
        # Decryption
        ctr = 1
        rev_cipher = sub_message[::-1]
        last_m = ord(rev_cipher[0]) ^ ord(rev_cipher[1])
        plain.append(chr(last_m))
        for c in rev_cipher[1:]:
            if ctr == (len(rev_cipher)-1):
                plain.append(chr(ord(c) ^ key))
            else:
                plain.append(chr(ord(c) ^ ord(rev_cipher[ctr+1])))
            ctr += 1
        final_plain = "".join([m for m in plain[::-1]])
    else:
        return "Please enter a correct method. {encrypt/decrypt}"
    return final_plain

# auxiliary function
def break_me(s: str) -> list:
    """
    Auxiliary function to divide the string to multiple strings
    according to the definition.
    'abcdefghij' -> ['aei','bfj','cg','dh']
    """
    return [s[i::4] for i in range(5)]

# Third task
# def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(msg: str, key_list: list, method: str) -> str:
#     """
#     >>> key_list = [0x20, 0x44, 0x54,0x20]
#     >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt')
#     'A&7D$@P'
#     >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt')
#     'A%5B#GW'
#     >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
#     ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'),
#     ...        key_list,'decrypt')
#     'abcdefg'
#     >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
#     ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'),
#     ...        key_list,'decrypt')
#     'Hellobello, it will work for a long message as well'
#     """
#     result = []
#     new_keys = [int(str(k)[:2]) for k in key_list]
#     if method == "encrypt":
#        # TODO
#         for k in new_keys:
#             result.append(encrypt_xor_with_changing_key_by_prev_cipher(i, new_keys[k], "encrypt") for i in break_me(msg))
#         return result
#     elif method == "decrypt":
#         # TODO
#         return result
#     else:
#         return "Please enter a correct method. {encrypt/decrypt}"

#     return result

if __name__ == "__main__":
    doctest.testmod()

    # Debug section:
    # key_list = [0x20, 0x44, 0x54,0x20]
    # print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt'))
