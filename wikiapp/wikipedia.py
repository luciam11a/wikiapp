import click
import requests
from pydantic import BaseModel, ValidationError

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


class Page(BaseModel):
    "A Page Dataclass to represent the return value from wikipedia"

    title: str  # the title of the wikipedia page
    extract: str  # the extract of a wikipedia page


def random_page(
    language: str = "en",  # the language you want to use, as a two character string.
) -> Page:  # returns a page object
    """Get a random page from wikipedia."""
    try:
        with requests.get(API_URL.format(language=language), timeout=10) as response:
            response.raise_for_status()
            data = response.json()
            return Page(**data)
        return data
    except (requests.RequestException, ValidationError) as error:
        message = str(error)
        raise click.ClickException(message) from error
