import click
from . import run

@click.command()
@click.argument('name')
def main(name):
    print(name + ":" + run())