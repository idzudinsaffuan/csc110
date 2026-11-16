def gcd(a : int, b: int) -> int:
    x = a
    y = b

    while y != 0:
        r = x % y
        x = y
        y = r

    return x

print(gcd(25,35))

def extended_euclidean_gcd(a : int, b : int) -> tuple(int, int, int):
