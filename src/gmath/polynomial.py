from gmath import factoring

class Polynomial:
    """
    A class to model polynomial equations.
    """
    
    def __init__(self, coeffs):
        """
        Initialize the Polynomial object.
        self.coeffs to be the coeffs parameter stripped of leading zeros.
        self.degree is the degree of the polynomial.
        
        Example:
        p = Polynomial([5, -5, -360])      # Equivalent to 5x^2 - 5x - 360
        p = Polynomial([0, 0, 5, 1, 0])    # Equivalent to 5x^2 + x
        """
        for c in coeffs:
            assert isinstance(c, int), "Non-integer coefficient."
        
        self.coeffs = []
        for i in range(len(coeffs)):
            if coeffs[i] != 0:
                self.coeffs = coeffs[i:]
                break
        
        assert self.coeffs, "Empty coefficients."
        
        self.degree = len(self.coeffs) - 1
        
    def factor_quadratic(self):
        """
        Return a tuple (a, b, c, d, e) representing the factored form of the quadratic,
        such that (a, b, c, d, e) = a(bx + c)(ex + d).
        
        Example:
        p = Polynomial(2, 7, 3)
        p.factor_quadratic()        # (1, 1, 3, 2, 1) (meaning (x + 3)(2x + 1))
        
        p = Polynomial(5, -5, 360)
        p.factor_quadratic()        # (5, 1, -9, 1, 8) (meaning 5(x - 9)(x + 8))
        """
        assert self.degree == 2, "Non-quadratic polynomial."
        
        constant = factoring.gcd(factoring.gcd(self.coeffs[0], self.coeffs[1]), self.coeffs[2])
        
        for i in range(len(self.coeffs)):
            self.coeffs[i] = int(self.coeffs[i] / constant)
        
        ac_factors = factoring.factor(abs(self.coeffs[0] * self.coeffs[2]))
        
        for i in range((len(ac_factors) // 2) + 1):
            if ac_factors[i] + ac_factors[-(i+1)] == self.coeffs[1]:
                expanded = [self.coeffs[0], ac_factors[i], ac_factors[-(i+1)], self.coeffs[2]]
                break
            elif abs(ac_factors[i] - ac_factors[-(i+1)]) == abs(self.coeffs[1]):
                if self.coeffs[1] < 0:
                    expanded = [self.coeffs[0], ac_factors[i], -1 * ac_factors[-(i+1)], self.coeffs[2]]
                    break
                else:
                    expanded = [self.coeffs[0], -1 * ac_factors[i], ac_factors[-(i+1)], self.coeffs[2]]
                    break
                
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