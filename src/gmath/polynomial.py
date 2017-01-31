class Polynomial:
    """
    A class to model polynomial equations.
    """
    
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.order = len(coeffs)
        
    def __str__(self):
        s = ""
        for i in reversed(range(self.order)):
            s += str(self.coeffs[-(i+1)])
            
            if i > 0:
                s += "x"
                if i > 1:
                    s += "^" + str(i)
            s += " + "
        return s[:-3]