import math

def gcf(a, b):
    """
    Return the greatest common factor of two positive integers.
    """
    if b == 0:
        return a
    else:
        return gcf(b, a % b)
            
def factor(n):
    """
    Return all positive factors of n as a list.
    """
    factors = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n / i:
                factors.append(int(n / i))
            
    return sorted(factors)

def prime_factor(n):
    """
    Return the prime factorization of n as a list.
    """
    i = 2
    factors = []
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
            
    if n > 1:
        factors.append(n)
        
    return factors

def reduce(a, b):
    """
    Return the reduced version of the fraction a/b as a tuple.
    """
    decimals = 0
    if len(str(a).split('.')[1]) > len(str(b).split('.')[1]):
        decimals = len(str(a).split('.')[1])
    else:
        decimals = len(str(b).split('.')[1])
    
    a = int(a * (10**decimals))
    b = int(b * (10**decimals))
    
    divisor = gcf(a, b)
    reduced = (int(a / divisor), (int(b / divisor)))
        
    return reduced

def simplify_radical(n):
    """
    Return the simplified version of sqrt(n) as a list.
    
    Example:
    simplify_radical(48)    # [4, 3], meaning 4 * sqrt(3)
    """
    radical = [1, n]
    pfactors = prime_factor(n)
    
    i = 1
    while i < len(pfactors):
        if pfactors[i] == pfactors[i-1]:
            radical[0] *= pfactors[i]
            radical[1] //= (pfactors[i]**2)
            del pfactors[i]
        i += 1
    
    return radical

def repeating_decimal(a, b):
    """
    Return the decimal representation of the fraction a/b as a string,
    including repeating decimal notation.
    
    Example:
    repeating_decimal(1, 6) # 0.1(6)
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