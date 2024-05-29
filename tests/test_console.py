from unittest.mock import Mock
from click.testing import CliRunner
from pytest_mock import MockFixture
import pytest
import requests

from wikiapp import console


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    return mocker.patch("wikiapp.wikipedia.random_page")


# def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
# runner.invoke(console.main, ["--language", "es"])
# mock_wikipedia_random_page.assert_called_with(language="es")


def test_main_print_title(runner: CliRunner, mock_requests_get: Mock) -> None:
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(runner: CliRunner, mock_requests_get: Mock) -> None:
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_users_correct_url(runner: CliRunner, mock_requests_get: Mock) -> None:
    runner.invoke(console.main)
    print("<<<", mock_requests_get)
    assert mock_requests_get.call_args[0] == (
        "https://en.wikipedia.org/api/rest_v1/page/random/summary",
    )


def test_main_succeeds(runner: CliRunner) -> None:
    result = runner.invoke(console.main)
    print(">>>", result)
    assert result.exit_code == 0


def test_main_fails_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


@pytest.mark.e2e
def test_main_suceeds_in_production(runner: CliRunner) -> None:
    result = runner.invoke(console.main)
    assert result.exit_code == 0
