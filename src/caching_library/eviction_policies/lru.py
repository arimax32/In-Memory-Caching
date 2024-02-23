from collections import OrderedDict 
from utils.cacheEntry import *

class LRU_Policy: 
    def __init__(self): 
        self.order = OrderedDict() 

    def process_get_entry(self, key): 
        if key in self.order:
            self.order.move_to_end(key)

    def evict_entry(self):
        return self.order.popitem(last=False)[0] 

    def process_put_entry(self, key, value): 
        if key in self.order: 
            self.order.move_to_end(key) 

        self.order[key] = CacheEntry(key,value)
    
    def process_delete_entry(self, key):
        if key in self.order:
            del self.order[key]
    
    def process_clear_entries(self):
        # Clear the existing dict
        self.order.clear()