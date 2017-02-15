import math

import gmath.factoring as factoring

def reduce(a, b):
    """
    Return the reduced version of the fraction a/b as a tuple.
    
    Example:
    reduce(8, 6)        # (4, 3)
    reduce(8.4, 6.2)    # (42, 31)
    """
    decimals = 0
    if len(str(float(a)).split('.')[1]) > len(str(float(b)).split('.')[1]):
        decimals = len(str(float(a)).split('.')[1])
    else:
        decimals = len(str(float(b)).split('.')[1])
    
    a = int(a * (10**decimals))
    b = int(b * (10**decimals))
    
    divisor = factoring.gcd(a, b)
    reduced = (int(a / divisor), (int(b / divisor)))
        
    return reduced

def repeating_decimal(a, b):
    """
    Return the decimal representation of the fraction a/b as a string,
    including repeating decimal notation.
    
    Example:
    repeating_decimal(1, 6)    # 0.1(6)
    """
    divided = []
    denom = b

    b = math.floor(a / denom);
    decimal = str(b) + ".";

    while a % denom != 0:
        a = (a - (b * denom)) * 10
        b = math.floor(a / denom)

        if a in divided:
            index = 2 + divided.index(a)
            decimal = decimal[0:index] + "(" + decimal[index:] + ")"
            break
        
        divided.append(a);
        decimal += str(b);

    return decimal;