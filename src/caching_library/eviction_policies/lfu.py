from collections import OrderedDict 
from utils.cacheEntry import *

class LFU_Policy:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

    def delete(self, key):
        pass
