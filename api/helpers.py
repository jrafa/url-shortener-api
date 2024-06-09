import random
from urllib.parse import urljoin

from api.constants import SHORT_CODE_MAX_LENGTH, SHORT_CODE_CHARS
from url_shortener.settings import DOMAIN_URL


def generate_short_code(length: int = SHORT_CODE_MAX_LENGTH) -> str:
    return "".join(random.choices(SHORT_CODE_CHARS, k=length))


def create_full_url(short_code: str) -> str:
    return urljoin(base=DOMAIN_URL, url=short_code)
