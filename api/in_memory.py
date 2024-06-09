class UrlMap:
    def __init__(self):
        self.URL_MAP = {}

    def add_key(self, key: str, value: str):
        self.URL_MAP[key] = value

    def key_exists(self, key: str) -> bool:
        return key in self.URL_MAP

    def key_not_exists(self, key: str) -> bool:
        return key not in self.URL_MAP

    def get_value(self, key: str) -> str:
        return self.URL_MAP[key]
