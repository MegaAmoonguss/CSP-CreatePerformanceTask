import sys
import re
import click
import math
import gmath

@click.group()
def cli():
    pass

@cli.command()
@click.argument('n')
def factor(n):
    """Returns the factors of an integer"""
    try:
        int(n)
    except ValueError:
        click.echo("Please enter an integer.", err=True)
        sys.exit(2)
    
    factors = gmath.factor(int(n))
    
    click.echo(f"The factors of {n} are {factors}.")
    
@cli.command()
@click.argument('n')
def primefactor(n):
    """Returns the prime factorization of an integer"""
    try:
        int(n)
    except ValueError:
        click.echo("Please enter an integer.", err=True)
        sys.exit(2)
    
    pfactors = gmath.prime_factor(int(n))
    
    factorization = ""
    for f in pfactors:
        factorization += str(f) + ' * '
    factorization = factorization[:-2]
    
    click.echo(f"The prime factorization of {n} is {factorization}.")
    
@cli.command()
@click.argument("fraction")
def reduce(fraction):
    """Reduces a given fraction in the form a/b"""
    try:
        a, b = [float(n) for n in fraction.split('/')]
        
        reduced_tup = gmath.reduce(a, b)
        
        if reduced_tup[1] == 1:
            reduced = str(reduced_tup[0])
        else:
            reduced = str(reduced_tup[0]) + "/" + str(reduced_tup[1])
    except ValueError:
        click.echo("Please a fraction in the format a/b where a and b are numbers.", err=True)
        sys.exit(2)
    
    click.echo(f"{fraction} = {reduced}")
    
@cli.command()
@click.argument("fraction")
def decimal(fraction):
    """Returns the decimal form of a fraction a/b"""
    try:
        a, b = [int(n) for n in fraction.split('/')]
    except ValueError:
        print("Please a fraction in the format a/b where a and b are integers.")
        sys.exit(2)
        
    decimal = gmath.repeating_decimal(a, b)
    print(f"{fraction} = {decimal}")
    
@cli.command()
@click.argument("decimal")
def fraction(decimal):
    """Returns the fraction form a decimal, including repeating"""
    try:
        frac = gmath.fraction(decimal)
    except AssertionError:
        print("Invalid decimal format.")
        sys.exit(2)
    print(f"{decimal} = {frac[0]}/{frac[1]}")
    
@cli.command()
@click.argument('n')
def sqrt(n):
    """Gives the exact square root of a number"""
    try:
        n = float(n)
        if int(n) == n:
            n = int(n)
    except ValueError:
        click.echo("Please enter a number.", err=True)
        sys.exit(2)
        
    if not isinstance(n, int):
        click.echo(f"The square root of {n} is {math.sqrt(n)}.")
        sys.exit(0)
        
    root = math.sqrt(n)
    if int(root) == root:
        click.echo(f"The square root of {n} is {int(root)}.")
    else:
        unformatted_root = gmath.simplify_radical(n)
        formatted_root = str(unformatted_root[0]) + " * sqrt(" + str(unformatted_root[1]) + ")"
        click.echo(f"The square root of {n} is {formatted_root}.")
        
@cli.command()
@click.argument('a')
@click.argument('b')
def gcd(a, b):
    """Finds the greatest common divisor of two numbers"""
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        click.echo("Please enter two integers.", err=True)
        sys.exit(2)
        
    divisor = math.gcd(a, b)
    click.echo(f"The greatest common divisor of {a} and {b} is {divisor}.")
    
@cli.command()
@click.argument('a')
@click.argument('b')
def lcm(a, b):
    """Finds the lowest common multiple of two numbers"""
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        click.echo("Please enter two integers.", err=True)
        sys.exit(2)
        
    multiple = gmath.lcm(a, b)
    click.echo(f"The least common multiple of {a} and {b} is {multiple}.")
    
@cli.command()
@click.argument("coeffs", nargs=3)
def quadratic(coeffs):
    """Returns a factored form of the quadratic with the entered coefficients"""
    try:
        a, b, c = [int(n) for n in coeffs]
    except ValueError:
        click.echo("Please enter three integers.", err=True)
        sys.exit(2)
        
    p = gmath.Polynomial([a, b, c])
    factored = p.factor()
    if factored:
        click.echo(f"{str(p)} = {gmath.factored_str(factored)}")
    else:
        click.echo(f"{str(p)} is not factorable.")
        
@cli.command()
@click.argument("points", nargs=-1)
def calcfunction(points):
    """Calculates the equation of a line or quadratic going through 2 or 3 given points"""
    if not len(points) in (2, 3):
        click.echo("Please enter two or three points in the format (x,y).", err=True)
        sys.exit(2)
    
    formatted = [None for _ in points]
    pattern = re.compile("\(-?[0-9]*,-?[0-9]*\)")
    for i in range(len(points)):
        if not pattern.match(points[i]):
            click.echo("Please enter points in the format (x,y).", err=True)
            sys.exit(2)  
        formatted[i] = [int(n) for n in points[i][1:-1].split(',')]
    
    p = gmath.Polynomial(points=formatted)
    click.echo(p)
    
if __name__ == "__main__":
    cli()