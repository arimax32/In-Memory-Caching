import threading
import time
from enum import Enum, auto 
from eviction_policies import *
from utils.cacheEntry import *

class EvictionPolicyType(Enum):
    LRU = auto()
    FIFO = auto()
    LIFO = auto()
    TTL = auto()

class Cache:
    def __init__(self, eviction_policy_type=EvictionPolicyType.LRU, capacity=5) -> None:
        self.cache_data = {}
        self.cache_buffer = capacity
        self.eviction_policy_type = eviction_policy_type
        self.lock = threading.Lock()
        self.eviction_policy = self.getPolicy()

    def getPolicy(self) :

        if self.eviction_policy_type == EvictionPolicyType.LRU:
            return lru.LRU_Policy()
        
        elif self.eviction_policy_type == EvictionPolicyType.FIFO:
            return fifo.FIFO_Policy()
        
        elif self.eviction_policy_type == EvictionPolicyType.LIFO:
            return lifo.LIFO_Policy()
        
        elif self.eviction_policy_type == EvictionPolicyType.TTL:
            self.lock = threading.RLock()
            return ttl.TTL_Policy(self.cache_data, self.cache_buffer, self.lock)
        
        else:
            raise ValueError("Invalid eviction policy type")

    def get(self, key) :
        with self.lock:
            self.eviction_policy.get(key)
            if key in self.cache_data:
                return self.cache_data[key].get_value()
            return None

    def put(self, key, value, duration=None) :
        with self.lock:
            if self.eviction_policy_type == EvictionPolicyType.TTL:
                self.eviction_policy.put(key, value, duration)
            else :
                if self.overflow():
                    removeKey = self.eviction_policy.evict_entry()
                    if removeKey is not None : 
                        del self.cache_data[removeKey]

                self.eviction_policy.process_put_entry(key, value)
                self.cache_data[key] = CacheEntry(key,value)
                
    def overflow(self):
        return len(self.cache_data) >= self.cache_buffer

    def delete(self, key):
        with self.lock:
            self.eviction_policy.delete(key)
            if key in self.cache_data:
                del self.cache_data[key]

    def clear(self):
        with self.lock:
            self.eviction_policy.clear()
            self.cache_data.clear()

if __name__ == '__main__':
    cache = Cache(EvictionPolicyType.TTL)
    start = time.time()
    cache.put('key1', 'value1', 40)
    cache.put('key2', 'value2')
    print(cache.get('key1'))
    time.sleep(6)
    print(cache.get('key2'))
    print(time.time()-start)
    # Sleep for a duration greater than the set expiration time
    time.sleep(12)
    print(time.time()-start)
    print(cache.get('key1'))
    print(time.time()-start)
    cache.put('key3','value3')
    print(time.time()-start)
    print(cache.get('key1'))
    
    # cache = Cache(EvictionPolicyType.FIFO,3)
    # cache.put("a",1)
    # cache.put("b",2)
    # cache.put("c",3)
    # print(cache.get("b"))
    # cache.put("d",4)
    # print(cache.cache_data)
    # print(cache.get("c"))
    # cache.put("b",33)
    # print(cache.cache_data)