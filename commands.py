import sys
import click
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
    
if __name__ == "__main__":
    cli()