import sys
import getopt
import math

def usage():
    print("Usage: gmath_py.py <operation> [input]")
    print()
    print("Operations:")
    print("-h --help            - shows the help menu")
    print("-f --factor          - returns the factors of the integer")
    print("-p --prime-factor    - returns the prime factors of the integer")
    print("-r --reduce          - reduces a given fraction in the form a/b")
    print("-s --square-root     - returns the exact square root of an integer, approximate for decimals")

def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hf:p:r:s:", ["help", "factor=", "prime-factor=", "--reduce=", "square-root="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    # TODO: add error handling
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
            
        elif opt in ("-f", "--factor"):
            factors = factor(int(arg))
            
            print("The factors of {0} are {1}".format(str(arg), str(factors)))
            
        elif opt in ("-p", "--prime-factor"):
            pfactors = prime_factor(int(arg))
            
            factorization = ""
            for f in pfactors:
                factorization += str(f) + ' * '
            factorization = factorization[:-2]
            
            print("The prime factorization of {0} is {1}".format(str(arg), factorization))
            
        elif opt in ("-r", "--reduce"):
            try:
                a, b = [int(n) for n in arg.split('/')]
                divisor = gcd(a, b)
                reduced = str(int(a / divisor)) + '/' + str(int(b / divisor))
                
                if reduced[-1] == '1':
                    reduced = reduced[:-2]
                
                print("{0} = {1}".format(arg, reduced))
            except ValueError:
                print("Please the fraction in the format a/b.")
        
        elif opt in ("-s", "--square-root"):
            if int(arg) == float(arg):
                arg = int(arg)
            else:
                arg = float(arg)
                print("The square root of {0} is {1}".format(arg, math.sqrt(arg)))
                
            root = math.sqrt(arg)
            if int(root) == root:
                print("The square root of {0} is {1}".format(arg, int(root)))
            else:
                unformatted_root = simplify_radical(arg)
                formatted_root = str(unformatted_root[0]) + "sqrt(" + str(unformatted_root[1]) + ")"
                print("The square root of {0} is {1}".format(arg, formatted_root))
            
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

def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a % b)
    
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