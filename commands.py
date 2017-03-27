import sys
import re
import click
import math
import sympy
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
@click.argument('n', type=int)
@pass_config
def factor(config, n):
    """Returns the factors of an integer."""
    factors = gmath.factor(int(n))
    
    click.echo(f"The factors of {n} are {factors}.", file=config.out)


@cli.command()
@click.argument('n', type=int)
@pass_config
def primefactor(config, n):
    """Returns the prime factorization of an integer."""
    pfactors = gmath.prime_factor(int(n))
    
    factorization = ""
    for f in pfactors:
        factorization += str(f) + ' * '
    factorization = factorization[:-3]
    
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
        
    dec = gmath.repeating_decimal(a, b)
    click.echo(f"{fraction} = {dec}", file=config.out)


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
@click.argument('n', type=float)
@pass_config
def sqrt(config, n):
    """Gives the exact square root of a number."""
    if n == int(n):
        n = int(n)
    else:
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
@click.argument('a', type=int)
@click.argument('b', type=int)
@pass_config
def gcd(config, a, b):
    """Finds the greatest common divisor of two numbers."""   
    divisor = math.gcd(a, b)
    click.echo(f"The greatest common divisor of {a} and {b} is {divisor}.", file=config.out)


@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
@pass_config
def lcm(config, a, b):
    """Finds the lowest common multiple of two numbers."""
    multiple = gmath.lcm(a, b)
    click.echo(f"The least common multiple of {a} and {b} is {multiple}.", file=config.out)


# To be deleted?
@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
@click.argument('c', type=int)
@pass_config
def quadratic(config, a, b, c):
    """Returns a factored form of the quadratic with the entered coefficients."""
    p = gmath.Polynomial([a, b, c])
    factored = p.factor()
    if factored:
        click.echo(f"{str(p)} = {gmath.factored_str(factored)}", file=config.out)
    else:
        click.echo(f"{str(p)} is not factorable.", file=config.out)


# Must decide between keeping this or making it independent of SymPy
@cli.command()
@click.argument("coeffs", nargs=-1, type=int)
@pass_config
def polynomial(config, coeffs):
    """Returns the factored form of the polynomial with the entered coefficients."""
    x = sympy.symbols('x')
    eq = coeffs[0] * x**(len(coeffs) - 1)
    for i in range(1, len(coeffs)):
        eq += coeffs[i] * x**(len(coeffs) - 1 - i)
    click.echo(str(eq) + " = " + str(eq.factor()), file=config.out)


@cli.command()
@click.argument("points", nargs=-1)
@pass_config
def calcfunction(config, points):
    """
    Calculates the equation of a line or quadratic going through 2 or 3
    given points.
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
    click.echo(f"y = {p}", file=config.out)


@cli.command()
@click.option("-t", "--term", type=int, default=0, help="Get the nth term of the sequence.")
@click.option("-n", "--next", type=int, default=0, help="Get the next n terms of the sequence.")
@click.argument("terms", nargs=-1, type=int)
@pass_config
def sequence(config, term, next, terms):
    """
    Calculates the equation of a sequence given the first few terms.
    To correctly identify an arithmetic or geometric sequence, 3 terms
    are needed, for a quadratic sequence, 4 terms are needed.
    """
    s = gmath.Sequence(terms)
    
    click.echo(f"Sequence type: {s.type}", file=config.out)
    click.echo(f"Equation: {s.equation}", file=config.out)
    if term > 0:
        try:
            click.echo(f"Term {term} of sequence: {s.get_term(term)}")
        except ValueError:
            click.echo("Term could not be found.")
            sys.exit(2)
    if next > 0:
        next_s = ""
        try:
            for i in range(1, next + 1):
                next_s += str(s.get_term(i + len(terms))) + ", "
        except ValueError:
            click.echo("Next terms could not be found.")
            sys.exit(2)
        click.echo(f"The next {next} terms of the sequence: {next_s[:-2]}")
    
if __name__ == "__main__":
    cli()
