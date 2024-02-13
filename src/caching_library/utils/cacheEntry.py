class CacheEntry():
    def __init__(self, key, value) -> None:
        self._key = key
        self._value = value

    def get_key(self):
        return self._key
    
    def get_value(self):
        return self._value