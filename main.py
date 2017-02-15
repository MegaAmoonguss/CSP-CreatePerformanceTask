import sys
import getopt
import math

from gmath import fraction
from gmath import factoring
from gmath import polynomial

def usage():
    print("Usage: main.py <operation> [input]")
    print()
    print("Operations:")
    print("-f --factor          - returns the factors of the integer")
    print("-p --prime-factor    - returns the prime factors of the integer")
    print("-r --reduce          - reduces a given fraction in the form a/b")
    print("-d --decimal         - returns the decimal form of a fraction a/b")
    print("-s --square-root     - gives the exact square root of a number")
    print("-g --gcd             - finds the greatest common divisor of two numbers")
    print("-l --lcm             - finds the lowest common multiple of two numbers")
    print("-q --quadratic       - returns a factored form of the quadratic with the")
    print("                       entered coefficients")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:p:r:d:s:g:l:q:", ["help", "factor=", "prime-factor=", "reduce=", "decimal=", "square-root=", "gcd=", "lcm=", "quadratic="])
    except getopt.GetoptError:
        print("Invalid input, pass '--help' for usage.")
        sys.exit(2)
    
    if not opts:
        print("Invalid input, pass '--help' for usage.")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            
        elif opt in ("-f", "--factor"):
            try:
                int(arg)
            except ValueError:
                print("Please enter an integer.")
                
            factors = factoring.factor(int(arg))
            
            print(f"The factors of {arg} are {factors}.")
            
        elif opt in ("-p", "--prime-factor"):
            try:
                int(arg)
            except ValueError:
                print("Please enter an integer.")
                continue
            
            pfactors = factoring.prime_factor(int(arg))
            
            factorization = ""
            for f in pfactors:
                factorization += str(f) + ' * '
            factorization = factorization[:-2]
            
            print(f"The prime factorization of {arg} is {factorization}.")
            
        elif opt in ("-r", "--reduce"):
            try:
                a, b = [float(n) for n in arg.split('/')]
                
                reduced_tup = fraction.reduce(a, b)
                
                if reduced_tup[1] == 1:
                    reduced = str(reduced_tup[0])
                else:
                    reduced = str(reduced_tup[0]) + "/" + str(reduced_tup[1])
                
                print(f"{arg} = {reduced}")
            except ValueError:
                print("Please a fraction in the format a/b where a and b are numbers.")
                
        elif opt in ("-d", "--decimal"):
            try:
                a, b = [int(n) for n in arg.split('/')]
                decimal = fraction.repeating_decimal(a, b)
                
                print(f"{arg} = {decimal}")
            except ValueError:
                print("Please a fraction in the format a/b where a and b are integers.")
        
        elif opt in ("-s", "--square-root"):
            try:
                arg = float(arg)
            except ValueError:
                print("Please enter a number.")
                continue
                
            if int(arg) == arg:
                arg = int(arg)
            else:
                print(f"The square root of {arg} is {math.sqrt(arg)}.")
                continue
                
            root = math.sqrt(arg)
            if int(root) == root:
                print(f"The square root of {arg} is {int(root)}.")
                continue
            else:
                unformatted_root = factoring.simplify_radical(arg)
                formatted_root = str(unformatted_root[0]) + " * sqrt(" + str(unformatted_root[1]) + ")"
                print(f"The square root of {arg} is {formatted_root}.")
        elif opt in ("-g", "--gcd"):
            try:
                a, b = [int(n) for n in arg.split()]
            except ValueError:
                print("Please enter two integers.")
                sys.exit(2)
                
            divisor = factoring.gcd(a, b)
            
            print(f"The greatest common divisor of {a} and {b} is {divisor}.")
        
        elif opt in ("-l", "--lcm"):
            try:
                a, b = [int(n) for n in arg.split()]
            except ValueError:
                print("Please enter two integers.")
                sys.exit(2)
                
            multiple = factoring.lcm(args[0], args[1])
            
            print(f"The least common multiple of {args[0]} and {args[1]} is {multiple}.")
            
        elif opt in ("-q", "--quadratic"):
            try:
                a, b, c = [int(n) for n in arg.split()]
            except ValueError:
                print("Please enter three integers.")
                sys.exit(2)
                
            p = polynomial.Polynomial([a, b, c])
            print(f"{str(p)} = {polynomial.factored_str(p.factor_quadratic())}")
    
if __name__ == '__main__':
    main()