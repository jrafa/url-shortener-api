import random

from api.constants import SHORT_CODE_MAX_LENGTH, SHORT_CODE_CHARS


def generate_short_code(length: int = SHORT_CODE_MAX_LENGTH) -> str:
    return "".join(random.choices(SHORT_CODE_CHARS, k=length))
