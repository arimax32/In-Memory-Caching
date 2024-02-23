from collections import deque 
from utils.cacheEntry import *

class FIFO_Policy: 
    def __init__(self, capacity): 
        self.order = deque()
        self.capacity = capacity 
    
    def process_get_entry(self, key): 
        pass 

    def evict_entry(self):
        return self.order.popleft().get_key()

    def process_put_entry(self, key, value): 
        self.order.append(CacheEntry(key,value))
    
    def process_delete_entry(self, key):
        pass

    def process_clear(self):
         # Clear the existing queue
        self.order.clear()