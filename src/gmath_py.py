import sys
import getopt
import math

def usage():
    print("Usage: gmath_py.py <operation> [input]")
    print()
    print("Operations:")
    print("-f --factor          - returns the factors of the integer")
    print("-p --prime-factor    - returns the prime factors of the integer")
    print("-r --reduce          - reduces a given fraction in the form a/b")
    print("-s --square-root     - gives the exact square root of a number")
    print("-g --gcf             - finds the greatest common divisor of two numbers")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:p:r:s:g", ["factor=", "prime-factor=", "reduce=", "square-root=", "gcf"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-f", "--factor"):
            try:
                int(arg)
            except ValueError:
                print("Please enter an integer.")
                
            factors = factor(int(arg))
            
            print(f"The factors of {arg} are {factors}.")
            
        elif opt in ("-p", "--prime-factor"):
            try:
                int(arg)
            except ValueError:
                print("Please enter an integer.")
            
            pfactors = prime_factor(int(arg))
            
            factorization = ""
            for f in pfactors:
                factorization += str(f) + ' * '
            factorization = factorization[:-2]
            
            print(f"The prime factorization of {arg} is {factorization}.")
            
        elif opt in ("-r", "--reduce"):
            try:
                a, b = [float(n) for n in arg.split('/')]
                
                reduced = reduce(a, b)
                
                print(f"{arg} = {reduced}")
            except ValueError:
                print("Please a fraction in the format a/b where a and b are numbers.")
        
        elif opt in ("-s", "--square-root"):
            try:
                arg = float(arg)
            except ValueError:
                print("Please enter a number.")
                sys.exit()
                
            if int(arg) == arg:
                arg = int(arg)
            else:
                print(f"The square root of {arg} is {math.sqrt(arg)}.")
                sys.exit()
                
            root = math.sqrt(arg)
            if int(root) == root:
                print(f"The square root of {arg} is {int(root)}.")
            else:
                unformatted_root = simplify_radical(arg)
                formatted_root = str(unformatted_root[0]) + " * sqrt(" + str(unformatted_root[1]) + ")"
                print(f"The square root of {arg} is {formatted_root}.")
        elif opt in ("-g", "--gcf"):
            if len(args) > 2:
                print("Please enter two integers.")
                sys.exit(2)
                
            try:
                args[0] = int(args[0])
                args[1] = int(args[1])
            except ValueError:
                print("Please enter two integers.")
                sys.exit(2)
                
            factor = gcf(args[0], args[1])
            
            print(f"The greatest common factor of {args[0]} and {args[1]} is {factor}.")
            
def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)
            
def factor(n):
    factors = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n / i:
                factors.append(int(n / i))
            
    return sorted(factors)

def prime_factor(n):
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
    decimals = 0
    if len(str(a).split('.')[1]) > len(str(b).split('.')[1]):
        decimals = len(str(a).split('.')[1])
    else:
        decimals = len(str(b).split('.')[1])
    
    a = int(a * (10**decimals))
    b = int(b * (10**decimals))
    
    divisor = gcf(a, b)
    reduced = str(int(a / divisor)) + '/' + str(int(b / divisor))
    
    if reduced[-1] == '1':
        reduced = reduced[:-2]
        
    return reduced

def simplify_radical(n):
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
    
if __name__ == '__main__':
    main()