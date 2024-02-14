# In Memory Thread Safe Caching Library

This is a lightweight and extensible in-memory caching library implemented in Python. It provides a thread-safe cache with support for various eviction policies, allowing you to manage and optimize data storage in memory.

## Features

- **Thread-Safe**: The caching library ensures thread safety, making it suitable for multi-threaded applications.
- **Eviction Policies**: Supports various eviction policies, including Least Recently Used (LRU), Least Frequently Used (LFU), First-In-First-Out (FIFO) and Time-To-Live(TTL) expiration feature 
- **Extensibility**: Easily extend the library by implementing custom eviction policies.
- **Simple Interface**: A straightforward API for adding, retrieving, and removing items from the cache.


## Usage

To use the caching library, first import the necessary classes and enums:

```python
from caching_library.cache import Cache, EvictionPolicyType

cache = Cache()
# Add entries to the cache
cache.put("key1", 1)
cache.put("key2", 2)
cache.put("key3", 3)
# Retrieve values from the cache
value1 = cache.get("key1")
# Remove a cache entry
cache.delete("key2")
# Clear the entire cache
cache.clear()
```

For particular eviction policies, use the EvictionPolicyType Enum

```python
cache = Cache(EvictionPolicyType.LIFO, capacity = 10)
# here in case of TTL policy capacity refers to the duration of each entry in memory
cache = Cache(EvictionPolicyType.TTL, capacity = 8) 
```
Here the EvictionPolicies supported are 
```python
class EvictionPolicyType(Enum):
    LRU = auto()
    FIFO = auto()
    LIFO = auto()
    TTL = auto()
```

## Running tests

To run the tests, use the following command in the tests/directory

```python
python test_eviction_policies.py
```
