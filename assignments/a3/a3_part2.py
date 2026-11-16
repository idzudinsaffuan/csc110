"""CSC110 Fall 2026 Assignment 3, Part 2: Block-Based RSA

Instructions (READ THIS FIRST!)
===============================

This Python module contains the functions you should complete for Part 2 of this assignment.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2026 CSC110 Teaching Team.
"""
# You may uncomment this statement to import the math module in this file
import math

from python_ta.contracts import check_contracts

###############################################################################
# Part (a): From strings to numbers
###############################################################################


@check_contracts
def base128_to_int(digits: list[int]) -> int:
    """Return the integer represented by the given base-128 representation.

    The input list has the units (128 ** 0) digit at the LAST index.

    Preconditions:
        - digits != []
        - all({0 <= d < 128 for d in digits})

    >>> base128_to_int([1])
    1
    >>> base128_to_int([3, 2, 4])  # 3 * (128 ** 2) + 2 * (128 ** 1) + 4 * (128 ** 0)
    49412
    >>> base128_to_int([72, 101, 108, 108, 111])
    19540948591

    NOTE: this function can be implemented by either a for loop or a comprehension.
    For practice, we strongly recommend trying both implementations.
    """
    sum_so_far = 0
    for i in range(len(digits)):
        sum_so_far += digits[i] * (128 ** (len(digits) - 1 - i))
    return sum_so_far


@check_contracts
def int_to_base128(n: int) -> list[int]:
    """Return the base-128 representation of the given number.

    The returned list has the units (128 ** 0) digit at the LAST index.
    The returned list should not have any leading zeros (i.e., the first element should be > 0).

    Preconditions:
    - n >= 1

    >>> int_to_base128(1)
    [1]
    >>> int_to_base128(49412)
    [3, 2, 4]

    HINTS: Here are two possible (ideas for) algorithms to solve this problem.
    You may use a different approach, as long as you use only programming elements and techniques
    allowed for this assignment. In particular, "recursion" is not permitted.

    APPROACH 1 ("big to small"):
        Start by computing the largest power of 128 that's less than or equal to n, and then compute the
        quotient (n // (128 ** ___)); that gives you the first element of the list.
        Update n in some way, and then repeat. You will find the math.log function useful.

    APPROACH 2 ("small to big"):
        Compute the remainder n % 128. That gives you the units digit (last element of the list).
        Update n in some way, and then repeat.
    """
    list_so_far = []
    x = n
    while x >= 1:
        list_so_far = [x % 128] + list_so_far
        x = x // 128
    return list_so_far

###############################################################################
# Part (b): Encrypting and decrypting blocks
###############################################################################


@check_contracts
def rsa_encrypt_block(public_key: tuple[int, int], plaintext: str) -> list[int]:
    """Encrypt the given plaintext using the recipient's public key.

    Preconditions:
        - public_key is a valid RSA public key (n, e)
        - public_key[0] >= 128
        - all({ord(c) < 128 for c in plaintext})
        - plaintext != ''
        - len(plaintext) is divisible by the block length

    NOTES:

    1. Use the pow function to compute a modular exponentiation, not ** and %.
       pow is much more efficient for larger numbers!
    2. You may find it useful to use range with THREE arguments, e.g. range(0, 10, 2).
       Experiment with this in the Python console!
    """
    n, e = public_key
    k = math.floor(math.log(n, 128))
    ciphertext_so_far = []
    for i in range(0, len(plaintext), k):
        block = plaintext[i: i + k]
        num_ord = [ord(c) for c in block]
        conv_128 = base128_to_int(num_ord)
        ciphertext_so_far.append(pow(conv_128, e, n))
    return ciphertext_so_far


@check_contracts
def rsa_decrypt_block(private_key: tuple[int, int, int], ciphertext: list[int]) -> str:
    """Decrypt the given ciphertext using the recipient's private key.

    Preconditions:
        - private_key is a valid RSA private key (p, q, d)
        - private_key[0] * private_key[1] >= 128
        - ciphertext != []
        - all({0 <= num < private_key[0] * private_key[1] for num in ciphertext})
    """
    str_so_far = ''
    p, q, d = private_key
    for i in ciphertext:
        decrypt_base128 = pow(i, d, p * q)
        list_int = int_to_base128(decrypt_base128)
        str_now_list_so_far = [chr(x) for x in list_int]
        str_now_so_far = ''
        for j in str_now_list_so_far:
            str_now_so_far = str_now_so_far + j
        str_so_far = str_so_far + str_now_so_far
    return str_so_far


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In VSCode, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['use-a-generator'],
        'extra-imports': ['math']
    })
