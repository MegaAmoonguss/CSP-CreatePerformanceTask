import math
import re
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

def fraction(dec):
    """
    Return the fraction form of the given decimal dec as a tuple (a, b), representing
    the fraction a/b. dec can be a float or string, and supports repeating decimal
    notation using parentheses around the repeating section.
    
    Example:
    fraction("0.08(3)")    # 1/12
    fraction(0.125)        # 1/8
    """
    if isinstance(dec, str):
        nonrepeat = re.compile("^[0-9]*(\.[0-9]*)$")
        repeat = re.compile("^[0-9]*(\.[0-9]*(\([0-9]+\)))$")
        assert nonrepeat.match(dec) or repeat.match(dec), "Improper format."
    else:
        assert isinstance(dec, float), "Improper format."
    
    if not '(' in dec:
        dec = float(dec)
        
    if isinstance(dec, float):
        numer = dec
        denom = 10**len(str(numer).split('.')[1])
        numer *= denom
    else:
        split = re.split(r"\(|\)|\.", dec)
        val1 = 10**(len(split[1]) + len(split[2]))
        val2 = 10**len(split[1])
        
        num = float(dec.replace('(', '').replace(')', ''))
        numer = (val1 * num) - math.floor(val2 * num)
        denom = val1 - val2
        return reduce(numer, denom)

    return reduce(numer, denom)