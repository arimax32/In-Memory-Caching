from collections import deque 
from utils.cacheEntry import *

class FIFO_Policy: 
    def __init__(self, capacity): 
        self.order = deque()
        self.capacity = capacity 
    
    def get(self, key): 
        pass 
    
    def print(self) :
        print(self.order)

    def put(self, key, value): 
        removeKey = None
        if len(self.order) >= self.capacity: 
            # Evict the first item from the cache (FIFO) 
            removeKey = self.order.popleft().get_key() 

        self.order.append(CacheEntry(key,value))
        return removeKey 
    
    def delete(self, key):
        pass