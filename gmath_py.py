import sys, getopt
import math

def usage():
    print("Usage: gmath_py.py <operation> [input]")
    print()
    print("Operations:")
    print("-h --help            - shows the help menu")
    print("-f --factor          - returns the factors of the integer input")
    print("-p --prime-factor    - returns the prime factors of the integer input")
    print("-r --reduce          - reduces a given fraction in the form a/b")

def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hf:p:r:", ["help", "factor=", "prime-factor=", "--reduce="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
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
    
    
if __name__ == '__main__':
    main()