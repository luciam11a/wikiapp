import click
import requests
from typing import Any

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language: str = "en") -> Any:
    """Get a random page from wikipedia."""
    try:
        with requests.get(API_URL.format(language=language), timeout=10) as response:
            response.raise_for_status()
            data = response.json()
        return data
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message) from error
