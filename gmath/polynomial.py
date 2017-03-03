from gmath import factoring

class Polynomial:
    """
    A class to model polynomial equations.
    """
    
    def __init__(self, coeffs=None, points=None):
        """
        Initialize the Polynomial object using either coefficients or 2/3 points on the line
        for 1st and 2nd degree polynomials (3 points to be added).
        self.coeffs are the coeffs parameter stripped of leading zeros.
        self.degree is the degree of the polynomial.
        
        Example:
        p = Polynomial(coeffs=[5, -5, -360])      # Equivalent to 5x^2 - 5x - 360
        p = Polynomial(coeffs=[0, 0, 5, 1, 0])    # Equivalent to 5x^2 + x
        p = Polynomial(points=[(0, 0), (1, 2)]    # Equivalent to 2x
        """
        assert bool(coeffs) ^ bool(points), "Invalid parameters."
        
        if coeffs:
            for c in coeffs:
                assert isinstance(c, int), "Non-integer coefficient."
            
            self.coeffs = []
            for i in range(len(coeffs)):
                if coeffs[i] != 0:
                    self.coeffs = coeffs[i:]
                    break
            
            assert self.coeffs, "Empty coefficients."
            
            self.degree = len(self.coeffs) - 1
        else:
            assert len(points) == 2, "Incorrect number of points."
            
            self.coeffs = []
            self.coeffs.append((points[1][1] - points[0][1]) / (points[1][0] - points[0][0]))
            self.coeffs.append(points[0][1] - (self.coeffs[0] * points[0][0]))
            self.degree = 1
        
    def factor(self):
        """
        Return a tuple (a, b, c, d, e) representing the factored form of the quadratic,
        such that (a, b, c, d, e) = a(bx + c)(ex + d). If the polynomial is not factorable,
        return None.
        
        Example:
        p = Polynomial(2, 7, 3)
        p.factor_quadratic()        # (1, 1, 3, 2, 1) (meaning (x + 3)(2x + 1))
        
        p = Polynomial(5, -5, 360)
        p.factor_quadratic()        # (5, 1, -9, 1, 8) (meaning 5(x - 9)(x + 8))
        """
        assert self.degree == 2, "Non-quadratic polynomial."
        for c in self.coeffs:
            assert isinstance(c, int), "Non-integer coefficient."
        
        coeffs = list(self.coeffs)
        constant = factoring.gcd(factoring.gcd(coeffs[0], coeffs[1]), coeffs[2])
        
        for i in range(len(coeffs)):
            coeffs[i] = int(coeffs[i] / constant)
        
        ac_factors = factoring.factor(abs(coeffs[0] * coeffs[2]))
        
        factorable = False
        for i in range((len(ac_factors) // 2) + 1):
            if ac_factors[i] + ac_factors[-(i+1)] == coeffs[1]:
                expanded = [coeffs[0], ac_factors[i], ac_factors[-(i+1)], coeffs[2]]
                factorable = True
                break
            elif abs(ac_factors[i] - ac_factors[-(i+1)]) == abs(coeffs[1]):
                if coeffs[1] < 0:
                    expanded = [coeffs[0], ac_factors[i], -1 * ac_factors[-(i+1)], coeffs[2]]
                    factorable = True
                    break
                else:
                    expanded = [coeffs[0], -1 * ac_factors[i], ac_factors[-(i+1)], coeffs[2]]
                    factorable = True
                    break
                
        if not factorable:
            return None
        
        divisors = [factoring.gcd(expanded[0], expanded[1]), factoring.gcd(expanded[2], expanded[3])]
        if expanded[0] < 0:
            divisors[0] *= -1
        if expanded[2] < 0:
            divisors[1] *= -1
        
        expanded[0] //= divisors[0]
        expanded[1] //= divisors[0]
        expanded[2] //= divisors[1]
        expanded[3] //= divisors[1]
        
        return (constant, divisors[0], divisors[1], expanded[0], expanded[1])
        
    def __str__(self):
        """
        Return the object as a properly formatted polynomial function.
        
        Example:
        p = Polynomial([5, -5, -360])
        str(p)                             # 5x^2 - 5x - 360
        
        p = Polynomial([0, 0, 5, 1, 0])
        str(p)                             # 5x^2 + x
        """
        s = ""
        for i in reversed(range(len(self.coeffs))):
            if i < self.degree:
                if self.coeffs[-(i+1)] < 0:
                    s += " - "
                elif self.coeffs[-(i+1)] > 0:
                    s += " + "
            
            if self.coeffs[-(i+1)] != 0:
                if self.coeffs[-(i+1)] != 1 or i == 0:
                    s += str(abs(self.coeffs[-(i+1)]))
                if i > 0:
                    s += "x"
                    if i > 1:
                        s += "^" + str(i)
        return s
    # End of Polynomial class
    
def factored_str(f):
    """
    Returns a formatted version of the tuple returned by factor_quadratic().
    
    Example:
    p = Polynomial(5, -5, -360)
    f = factor(p)
    factored_str(f)                # 5(x - 9)(x + 8)
    """
    assert len(f) == 5, "Invalid input: incorrect length."
    
    for c in f:
        assert isinstance(c, int), "Invalid input: non-int value."
    
    s = ""
    if f[0] < 0:
        s += "-"
    if f[0] != 1:
        s += str(f[0])
    s += "("
    if f[1] < 0:
        s += "-"
    if abs(f[1]) != 1:
        s += str(abs(f[1]))
    s += "x"
    if f[2] < 0:
        s += " - " + str(abs(f[2]))
    else:
        s += " + " + str(f[2])
    s += ")("
    if f[0] < 0:
        s += "-"
    if abs(f[3]) != 1:
        s += str(abs(f[3]))
    s += "x"
    if f[4] < 0:
        s += " - " + str(abs(f[4]))
    else:
        s += " + " + str(f[4])
    s += ")"
    
    return s