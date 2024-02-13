from collections import deque 
from utils.cacheEntry import *

class LIFO_Policy: 
    def __init__(self, capacity): 
        self.order = deque()
        self.capacity = capacity 

    def get(self, key): 
        pass 

    def put(self, key, value): 
        removeKey = None
        if len(self.order) >= self.capacity: 
            # Evict the last item from the cache (LIFO) 
            removeKey = self.order.pop().get_key()
    
        self.order.append(CacheEntry(key, value)) 
        return removeKey
    
    def delete(self, key):
        pass

    def clear(self):
        # Clear the existing queue
        self.order.clear()