#!/usr/bin/env python3
"""First-In First-Out caching module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represent an obj that allows the storage and
    retrieval of items from a dict with a FIFO
    removal mechanism when reaching limit.
    """
    def __init__(self):
        """Initialize cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve an item by its key
        """
        return self.cache_data.get(key, None)
