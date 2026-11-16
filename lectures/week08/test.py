def all_cool(s:str) -> bool:
    for i in s:
        if i not in 'cool':
            return False
    return True

result = all_cool('coooooooooooll')
print(result)


def encrypt_otp(k: str, plaintext: str) -> str:
    """Return the encrypted message of plaintext using the key k with the
    one-time pad cryptosystem.

    Preconditions:
        - len(k) >= len(plaintext)
        - all({ord(c) < 128 for c in plaintext})
        - all({ord(c) < 128 for c in k})

    >>> encrypt_otp('david', 'HELLO')
    ',&B53'
    """
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += (plaintext[i] + ord(k[i])) % 128
    return ciphertext

def decrypt_otp(k: str, ciphertext: str) -> str:
    """Return the decrypted message of ciphertext using the key k with the
    one-time pad cryptosystem.

    Preconditions:
        - len(k) >= len(ciphertext)
        - all({ord(c) < 128 for c in ciphertext})
        - all({ord(c) < 128 for c in k})

    >>> decrypt_otp('david', ',&B53')
    'HELLO'
    """
    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext += (ciphertext[i] - ord(k[i]))
    return plaintext


def break_diffie_hellman(p: int, g: int, g_a: int, g_b: int) -> int:
    """Return the shared Diffie-Hellman secret key obtained from the eavesdropped information.

    Remember that the secret key is (g ** (a * b)) % p, where a and b are the
    secret exponents chosen by Alice and Bob.
    You'll need to find at least one of a and b to compute the secret key.

    Preconditions:
        - p, g, g_a, and g_b are the values exchanged between Alice and Bob
          in the Diffie-Hellman algorithm

    >>> p = 23
    >>> g = 2
    >>> g_a = 9  # g ** 5 % p
    >>> g_b = 8  # g ** 14 % p
    >>> break_diffie_hellman(p, g, g_a, g_b)  # g ** (5 * 14) % p
    16
    """
    for i in range(1,p):
        if g_a == g ** i % p:
            return (g_b ** i) %

        



    


    








