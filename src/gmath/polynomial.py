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
        p = Polynomial([5, -5, 360])       # Equivalent to 5x^2 - 5x + 360
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
        
        self.degree = len(self.coeffs)
        
    def __str__(self):
        """
        Return the object as a properly formatted polynomial function.
        
        Example:
        p = Polynomial([5, -5, 360])
        str(p)                             # 5x^2 - 5x + 360
        
        p = Polynomial([0, 0, 5, 1, 0])
        str(p)                             # 5x^2 + x
        """
        s = ""
        for i in reversed(range(self.degree)):
            if i < self.degree - 1:
                if self.coeffs[-(i+1)] < 0:
                    s += " - "
                elif self.coeffs[-(i+1)] > 0:
                    s += " + "
            
            if self.coeffs[-(i+1)] != 0:
                if self.coeffs[-(i+1)] != 1:
                    s += str(abs(self.coeffs[-(i+1)]))
                if i > 0:
                    s += "x"
                    if i > 1:
                        s += "^" + str(i)
            
        return s