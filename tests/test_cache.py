import unittest
import sys
sys.path.append('../src/caching_library')

from cache import Cache

class TestCache(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super(TestCache, self).__init__(*args, **kwargs)
        self.cache = None

    def setUpCache(self, max_size=None):
        if max_size:
            return Cache(capacity=max_size)
        
        return Cache()

    def test_cache_put_get(self):
        self.cache = self.setUpCache(max_size=3)
        self.create_testcases()

        value1 = self.cache.get("key1")
        value2 = self.cache.get("key2")

        self.assertEqual(value1, "1")
        self.assertEqual(value2, "2")

    def test_cache_clear(self):
        self.cache = self.setUpCache()
        self.create_testcases()

        self.cache.clear()

        self.assertIsNone(self.cache.get("key1"))
        self.assertIsNone(self.cache.get("key2"))

    def test_cache_delete(self):
        self.cache = self.setUpCache()
        self.create_testcases()

        self.cache.delete("key1")

        value1 = self.cache.get("key1")
        value2 = self.cache.get("key2")
        
        self.assertIsNone(value1)
        self.assertEqual(value2, "2")

    def create_testcases(self):
        self.cache.put("key1", "1")
        self.cache.put("key2", "2")

if __name__ == '__main__':
    unittest.main()
