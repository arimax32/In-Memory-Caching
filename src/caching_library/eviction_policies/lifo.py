from collections import deque 
from utils.cacheEntry import *

class LIFO_Policy: 
    def __init__(self): 
        self.order = deque()

    def process_get_entry(self, key): 
        pass 

    def evict_entry(self):
        return self.order.pop().get_key()

    def process_put_entry(self, key, value): 
        self.order.append(CacheEntry(key, value)) 
    
    def process_delete_entry(self, key):
        pass

    def process_clear_entries(self):
        # Clear the existing queue
        self.order.clear()