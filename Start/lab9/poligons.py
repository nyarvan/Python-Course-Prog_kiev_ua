import math

def area_of_triangle(a, b, c):
    """
    Returns area of triangle
    :param a:
    :param b:
    :param c:
    :return: None, if .....
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return None
    if not (a + c > b and a + b > c and b + c > a):
        return None

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area