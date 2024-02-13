import time
import unittest
import math
import sys
sys.path.append('../src/caching_library')

from cache import Cache, EvictionPolicyType

class TestEvictionPolicies(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super(TestEvictionPolicies, self).__init__(*args, **kwargs)
        self.test_keys = ["key1", "key4", "key3", "key2", "key5"]
        self.test_values = ["1", "4", "3", "2", "5"]

    def setUpCache(self, eviction_policy_type, max_size=None):
        if max_size:
            return Cache(eviction_policy_type, capacity=max_size)
        
        return Cache(eviction_policy_type)
    
    def get_test_keys(self):
        return self.test_keys
    
    def create_testcases(self, cache, length=None):
        if length is None:
            length = math.inf

        for i in range(min(length, len(self.test_keys))):
            cache.put(self.test_keys[i],self.test_values[i])

    def assertion_test(self, cache, deleteKey, keys):
        for i, key in enumerate(keys):
            value = cache.get(key)
            if key == deleteKey:
                self.assertIsNone(value)
            else:
                self.assertEqual(value, self.test_values[i])

class TestLRUCache(TestEvictionPolicies):
    def __init__(self, *args, **kwargs) -> None:
        super(TestLRUCache, self).__init__(*args, **kwargs)
        self.cache = None
        self.eviction_policy = EvictionPolicyType.LRU

    def setUp(self, buffer=None):
        self.cache = super().setUpCache(self.eviction_policy, buffer)
        self.create_testcases(cache=self.cache)

    def test_lru_eviction_policy(self):
        self.setUp()

        self.cache.get("key1")
        self.cache.get("key3")

        self.cache.put("key0", 0)

        keys = super().get_test_keys()
        super().assertion_test(self.cache, "key4", keys)

class TestLIFOCache(TestEvictionPolicies):
    def __init__(self, *args, **kwargs) -> None:
        super(TestLIFOCache, self).__init__(*args, **kwargs)
        self.cache = None
        self.eviction_policy = EvictionPolicyType.LIFO

    def setUp(self, buffer=None):
        self.cache = super().setUpCache(self.eviction_policy, buffer)
        self.create_testcases(cache=self.cache)

    def test_lifo_eviction_policy(self):
        self.setUp(buffer=4)

        self.cache.put("key6", "6")

        keys = super().get_test_keys()
        super().assertion_test(self.cache, "key2", keys[:4])

class TestFIFOCache(TestEvictionPolicies):
    def __init__(self, *args, **kwargs) -> None:
        super(TestFIFOCache, self).__init__(*args, **kwargs)
        self.cache = None
        self.eviction_policy = EvictionPolicyType.FIFO

    def setUp(self, buffer=None):
        self.cache = super().setUpCache(self.eviction_policy, buffer)
        self.create_testcases(cache=self.cache)
    
    def test_fifo_eviction_policy(self):
        self.setUp()
        
        self.cache.put("key7", 7)

        keys = super().get_test_keys()
        super().assertion_test(self.cache, "key1", keys)

class TestTTLCache(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super(TestTTLCache, self).__init__(*args, **kwargs)
        self.cache = None
        self.eviction_policy_type = EvictionPolicyType.TTL

    def setUpCache(self, duration=None):
        if duration:
            return Cache(self.eviction_policy_type, capacity=duration)
        
        return Cache(self.eviction_policy_type)

    def test_ttl_eviction_policy(self):
        # Set a cache with a TTL of 5 seconds which is by default anyways
        self.cache = self.setUpCache(duration=5) 

        self.cache.put("key1", "1",10)
        self.cache.put("key2", "2")
        self.cache.put("key3", "3")

        # TTL of 'key2 and 'key3 is both 5 seconds hence this sleep makes them evict
        time.sleep(6)

        value = self.cache.get("key1")

        self.assertIsNone(self.cache.get(2))
        self.assertIsNone(self.cache.get(3))
        self.assertEqual(value, "1")

if __name__ == '__main__':
    unittest.main()
