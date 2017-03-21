from gmath import Polynomial

class Sequence:
    """
    A class to model sequences.
    """
    
    def __init__(self, terms):
        """
        Initialize Sequence object by figuring out what kind of sequence the terms are a part of
        and the equation for the nth term.
        """
        if len(terms) > 1 and terms[1:] == terms[:-1]:
            type = "equal"
            self.equation = str(terms[0])
        elif is_arithmetic(terms):
            self.type = "arithmetic"
            self.equation = f"{terms[0]} + (n - 1) * {terms[1] - terms[0]}"
            self.disp_equation = self.equation.replace("**", '^')
        elif is_geometric(terms):
            self.type = "geometric"
            self.equation = f"{terms[0]} * {terms[1] - terms[0]}**(n - 1)"
            self.disp_equation = self.equation.replace("**", '^')
        elif is_quadratic(terms):
            self.type = "quadratic"
            p = Polynomial(points=((1, terms[0]), (2, terms[1]), (3, terms[2])))
            self.equation = f"{p.coeffs[0]} * n**2 + {p.coeffs[1]} * n + {p.coeffs[2]}"
            self.disp_equation = str(p)
        else:
            raise ValueError("No sequence found")
    
    def get_term(self, n):
        """
        Return the nth value of the sequence. Starts at index 0.
        """
        retval = eval(self.equation.replace('n', str(n)))
        if retval == int(retval):
            return int(retval)
        return retval

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