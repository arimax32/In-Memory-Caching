from collections import OrderedDict 
from utils.cacheEntry import *

class LFU_Policy: 
    def __init__(self): 
        # data structures
        pass

    def process_get_entry(self, key): 
        pass

    def put(self, key, value):
        pass 
        # removeKey = None
        # if key in self.order: 
        #     self.order.move_to_end(key) 
        # else :
        #     if len(self.data_structure) >= self.capacity: 
        #         # Evict the least recently used item from the cache (LRU) 
        #         removeKey = self.order.popitem(last=False)[0] 

        # self.order[key] = CacheEntry(key,value)
        # return removeKey
    
    def overflow(self, key, capacity) :
        pass
    
    def process_delete_entry(self, key):
        if key in self.order:
            del self.order[key]
    
    def process_clear(self):
        # Clear the existing dict
        self.order.clear()