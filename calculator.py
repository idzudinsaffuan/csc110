def square(x: float) -> float:
    """return x squared
    for example:
    >> square(3.0)
    9.0
    >> square(2.5)
    6.25
    """
    return x ** 2

def DistPoint(p1: list, p2: list) -> float:
    """return distance between two points
    p1 and p2 in list: (x1, y1) and (x2, y2) respectively, x and y are float
    """
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return (square(x1-x2) + square(y1-y2)) ** 0.5

def square_sum(nums: list) -> float:
    """return the sum of squares (not square of sum!)
    """
    num1 = nums[0]
    num2 = nums[1]
    return square(num1) + square(num2)
