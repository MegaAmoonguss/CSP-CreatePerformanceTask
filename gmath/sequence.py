from gmath import Polynomial

class Sequence:
    """
    A class to model sequences.
    """
    
    def __init__(self, terms):
        """
        Initialize Sequence object by figuring out what kind of sequence the terms are a part of
        and the equation for the nth term.
        0 = all values are equal
        1 = arithmetic
        2 = geometric
        3 = quadratic
        """
        if len(terms) > 1 and terms[1:] == terms[:-1]:
            self.type = 0
            self.equation = str(terms[0])
        elif is_arithmetic(terms):
            self.type = 1
            p = Polynomial(points=terms[:2])
            self.equation = f"{p.coeffs[1]} * x + {p.coeffs[2]}"
        elif is_geometric(terms):
            self.type = 2
            # equation to be implemented
        elif is_quadratic(terms):
            self.type = 3
            p = Polynomial(points=terms[:3])
            self.equation = f"{p.coeffs[0]} * x**2 + {p.coeffs[1]} * x + {p.coeffs[2]}"

def is_arithmetic(terms):
    """
    Checks if given terms make up an arithmetic sequence. Length of terms must be at least 3.
    """
    if len(terms) < 3:
        return False
    
    d = terms[1] - terms[0]
    for i in range(2, len(terms)):
        if terms[i] - terms[i - 1] != d:
            return False
    return True

def is_geometric(terms):
    """
    Checks if given terms make up a geometric sequence. Length of terms must be at least 3.
    """
    if len(terms) < 3:
        return False
    
    d = terms[1] / terms[0]
    for i in range(2, len(terms)):
        if terms[i] / terms[i - 1] != d:
            return False
    return True

def is_quadratic(terms):
    """
    Checks if given terms make up a quadratic sequence. Length of terms must be at least 4.
    """
    if len(terms) < 4:
        return False
    
    if is_arithmetic(terms):
        return False
    
    diffs = []
    for i in range(1, len(terms)):
        diffs.append(terms[i] - terms[i - 1])
    
    d = diffs[1] - diffs[0]
    for i in range(2, len(diffs)):
        if diffs[i] - diffs[i - 1] != d:
            return False
    return True