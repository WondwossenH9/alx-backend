#!/usr/bin/env python3
"""Basic caching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows the storage and
    retrieval of items from a dictionary.
    """
    def put(self, key, item):
        """Add an item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by its key
        """
        return self.cache_data.get(key, None)
