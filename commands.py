import sys
import re
import click
import math
import gmath

class Config:
    
    def __init__(self):
        pass

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option("-o", "--out", default='-', type=click.File('w'), help="Output to a file.")
@pass_config
def cli(config, out):
    config.out = out

@cli.command()
@click.argument('n')
@pass_config
def factor(config, n):
    """Returns the factors of an integer."""
    try:
        int(n)
    except ValueError:
        click.echo("Please enter an integer.", err=True)
        sys.exit(2)
    
    factors = gmath.factor(int(n))
    
    click.echo(f"The factors of {n} are {factors}.", file=config.out)
    
@cli.command()
@click.argument('n')
@pass_config
def primefactor(config, n):
    """Returns the prime factorization of an integer."""
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
    
    click.echo(f"The prime factorization of {n} is {factorization}.", file=config.out)
    
@cli.command()
@click.argument("fraction")
@pass_config
def reduce(config, fraction):
    """Reduces a given fraction in the form a/b."""
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
    
    click.echo(f"{fraction} = {reduced}", file=config.out)
    
@cli.command()
@click.argument("fraction")
@pass_config
def decimal(config, fraction):
    """Returns the decimal form of a fraction a/b."""
    try:
        a, b = [int(n) for n in fraction.split('/')]
    except ValueError:
        click.echo("Please a fraction in the format a/b where a and b are integers.", err=True)
        sys.exit(2)
        
    decimal = gmath.repeating_decimal(a, b)
    click.echo(f"{fraction} = {decimal}", file=config.out)
    
@cli.command()
@click.argument("decimal")
@pass_config
def fraction(config, decimal):
    """Returns the fraction form a decimal, including repeating."""
    try:
        frac = gmath.fraction(decimal)
    except AssertionError:
        click.echo("Invalid decimal format.", err=True)
        sys.exit(2)
    click.echo(f"{decimal} = {frac[0]}/{frac[1]}", file=config.out)
    
@cli.command()
@click.argument('n')
@pass_config
def sqrt(config, n):
    """Gives the exact square root of a number."""
    try:
        n = float(n)
        if int(n) == n:
            n = int(n)
    except ValueError:
        click.echo("Please enter a number.", err=True)
        sys.exit(2)
        
    if not isinstance(n, int):
        click.echo(f"The square root of {n} is {math.sqrt(n)}.", file=config.out)
        sys.exit(0)
        
    root = math.sqrt(n)
    if int(root) == root:
        click.echo(f"The square root of {n} is {int(root)}.", file=config.out)
    else:
        unformatted_root = gmath.simplify_radical(n)
        formatted_root = str(unformatted_root[0]) + " * sqrt(" + str(unformatted_root[1]) + ")"
        click.echo(f"The square root of {n} is {formatted_root}.", file=config.out)
        
@cli.command()
@click.argument('a')
@click.argument('b')
@pass_config
def gcd(config, a, b):
    """Finds the greatest common divisor of two numbers."""
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        click.echo("Please enter two integers.", err=True)
        sys.exit(2)
        
    divisor = math.gcd(a, b)
    click.echo(f"The greatest common divisor of {a} and {b} is {divisor}.", file=config.out)
    
@cli.command()
@click.argument('a')
@click.argument('b')
@pass_config
def lcm(config, a, b):
    """Finds the lowest common multiple of two numbers."""
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        click.echo("Please enter two integers.", err=True)
        sys.exit(2)
        
    multiple = gmath.lcm(a, b)
    click.echo(f"The least common multiple of {a} and {b} is {multiple}.", file=config.out)
    
@cli.command()
@click.argument('a')
@click.argument('b')
@click.argument('c')
@pass_config
def quadratic(config, a, b, c):
    """Returns a factored form of the quadratic with the entered coefficients."""
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        click.echo("Please enter three integers.", err=True)
        sys.exit(2)
        
    p = gmath.Polynomial([a, b, c])
    factored = p.factor()
    if factored:
        click.echo(f"{str(p)} = {gmath.factored_str(factored)}", file=config.out)
    else:
        click.echo(f"{str(p)} is not factorable.", file=config.out)
        
@cli.command()
@click.argument("points", nargs=-1)
@pass_config
def calcfunction(config, points):
    """
    Calculates the equation of a line or quadratic going through
    2 or 3 given points.
    """
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
    click.echo(p, file=config.out)

@cli.command()
@click.argument("terms", nargs=-1)
@pass_config
def sequence(config, terms):
    """
    Calculates the equation of a sequence given the first few terms.
    To correctly identify an arithmetic or geometric sequence, 3 terms
    are needed, for a quadratic sequence, 4 terms are needed.
    """
    try:
        terms = [int(t) for t in terms]
    except ValueError:
        click.echo("Invalid input.", err=True)
        sys.exit(2)
    
    try:
        s = gmath.Sequence(terms)
    except ValueError:
        click.echo("No sequence found.")
        sys.exit(2)
    
    click.echo(f"Sequence type: {s.type}", file=config.out)
    click.echo(f"Equation: {s.equation.replace('**', '^')}", file=config.out)
    
if __name__ == "__main__":
    cli()