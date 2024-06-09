import pytest

from api.helpers import generate_short_code, create_full_url
from url_shortener.settings import DOMAIN_URL


def test_generate_short_code_with_invalid_length():
    length = 10
    result = generate_short_code(length=length)

    assert len(result) == length
    assert isinstance(result, str)


@pytest.mark.parametrize("short_code", ["ABC123", "XyZ987"])
def test_create_full_url_with_success(short_code: str):
    result = create_full_url(short_code=short_code)

    assert result == f"{DOMAIN_URL}/{short_code}"
    assert isinstance(result, str)
