p = [3.0, 4.0]
# MARKER A

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the distance between points (x1, y1) and (x2, y2),
    rounded to two decimal places.

    >>> calculate_distance(0.0, 0.0, 3.0, 4.0)
    5.0
    """
    # MARKER B
    dx_squared = square(x1 - x2)
    dy_squared = square(y1 - y2)
    return round((dx_squared + dy_squared) ** 0.5, 2)

def square(x: float) -> float:
    """Return x squared.

    >>> square(3.0)
    9.0
    >>> square(2.5)
    6.25
    """
    # MARKER C
    return x ** 2

distance = calculate_distance(0.0, 0.0, p[0], p[1])
# MARKER D

print(distance)
