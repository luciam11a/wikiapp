from wikiapp import wikipedia
from unittest.mock import Mock


def test_random_page_uses_language(mock_requests_get: Mock) -> None:
    wikipedia.random_page(language="es")
    args, _ = mock_requests_get.call_args
    assert "es.wikipedia.org" in args[0]
