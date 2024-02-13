import threading
from utils.cacheEntry import *
from utils.timeBoundQueue import TimeBoundQueue

class TTL_Policy:
    def __init__(self, cache = dict(), duration=5, lock=None):
        self.cache_data = cache
        self.time = duration
        if lock is None:
            self.lock = threading.RLock()
        else:
            self.lock = lock
        self.delayed_queue = TimeBoundQueue()
        self.eviction_thread = threading.Thread(target=self.eviction_thread_task, daemon=True)
        self.eviction_thread.start()

    def get(self, key):
        pass

    def put(self, key, value, duration=None):
        with self.lock:
            if duration is None:
                duration = self.time
                
            self.cache_data[key] = CacheEntry(key,value)
            self.delayed_queue.push(duration, lambda: self.evict_entry(key))

    def delete(self, key):
        pass
        
    def evict_entry(self, key):
        with self.lock:
            if key in self.cache_data:
                del self.cache_data[key]

    def eviction_thread_task(self):
        while True:
            eviction_task = self.delayed_queue.pop()
            if eviction_task:
                eviction_task()