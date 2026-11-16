# helper function
def naive_gcd(m: int, n: int) -> int:
    """Return the gcd of m and n."""
    if m == 0:
        return abs(n)
    elif n == 0:
        return abs(m)
    else:
        possible_divisors = range(1, min(abs(m), abs(n)) + 1)
        return max({d for d in possible_divisors
                    if divides(d, m) and divides(d, n)})

def divides(d: int, n: int) -> bool:
    """Return whether d divides n.
    >>> divides(3, 9)   # Is 9 divisible by 3? (Yes)
    True
    >>> divides(3, 10)  # Is 10 divisible by 3? (No)
    False
    """
    if d == 0:
        return n == 0
    else:
        return n % d == 0


def euclidean(a: int, b: int) -> int:
    x = abs(a)
    y = abs(b)

    while y != 0:
        r = x % y

        x = y
        y = r

    return x


def extended_euclidean_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that
    gcd(a, b) == p * a + q * b.
    Preconditions:
    - a >= 0
    - b >= 0
    >>> extended_euclidean_gcd(10, 3)
    (1, 1, -3)
    """
    x, y = a, b

    # Initialize px, qx, py, and qy
    px, qx = 1, 0  # Since x == a == 1 * a + 0 * b
    py, qy = 0, 1  # Since y == b == 0 * a + 1 * b

    while y != 0:
        # assert math.gcd(a, b) == math.gcd(x, y)  # Loop Invariant 1
        assert x == px * a + qx * b                # Loop Invariant 2
        assert y == py * a + qy * b                # Loop Invariant 3

        q, r = divmod(x, y)  # quotient and remainder when x is divided by y
        # Update x and y
        x, y = y, r
        # Update px, qx, py, and qy
        px, qx, py, qy = py,  qy, px - q*py, qx - q*qy

    return (x, px, qx)

#exercise 1 starts here
import math

def modular_inverse(a: int, n: int) -> int:
    """Return the inverse of a modulo n, in the range 0 to n - 1 inclusive.

    Preconditions:
    - math.gcd(a,n) == 1
    - n > 0
    -

    Postconditions:
    - n - 1 >= $returnvalue >= 0
    - (a *  $returnvalue - 1) % n == 0

    >>> modular_inverse(10, 3)  # 10 * 1 is equivalent to 1 modulo 3
    1
    >>> modular_inverse(3, 10)  # 3 * 7 is equivalent to 1 modulo 10
    7
    """
    gcd, p, n = extended_euclidean_gcd(a, n)
    return p


print(modular_inverse(3,10))
