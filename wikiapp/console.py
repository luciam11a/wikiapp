import textwrap

import click

from wikiapp import __version__
from wikiapp.wikipedia import random_page


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Get random page from wikipedia in given language",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:  # this is a console function so returns nothing
    """
    this is the console interface to 'random_page' function in wikipedia.py
    """
    """The ultramodern Python project."""
    page = random_page(language=language)
    title = page.title
    extract = page.extract
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))


if __name__ == "__main__":
    main()
