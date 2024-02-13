from collections import OrderedDict 
from utils.cacheEntry import *

class LRU_Policy: 
    def __init__(self, capacity): 
        self.order = OrderedDict() 
        self.capacity = capacity 

    def get(self, key): 
        if key in self.order:
            self.order.move_to_end(key)

    def print(self) :
        print(self.order)

    def put(self, key, value): 
        removeKey = None
        if key in self.order: 
            self.order.move_to_end(key) 
        else :
            if len(self.order) >= self.capacity: 
                # Evict the least recently used item from the cache (LRU) 
                removeKey = self.order.popitem(last=False)[0] 

        self.order[key] = CacheEntry(key,value)
        return removeKey
    
    def delete(self, key):
        if key in self.order:
            del self.order[key]