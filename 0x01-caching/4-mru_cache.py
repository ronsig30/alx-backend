#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item if the key already exists
            self.cache_data[key] = item
            """ Move the key to the end of the OrderedDict to mark it as recent
            ly used"""
            self.order.move_to_end(key)
        else:
            # Add new item to the cache
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used item (last item in OrderedDict)
                most_recent_key, _ = self.order.popitem(last=True)
                del self.cache_data[most_recent_key]
                print(f"DISCARD: {most_recent_key}")

            # Add new item to cache
            self.cache_data[key] = item
            self.order[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as recently used
        self.order.move_to_end(key)
        return self.cache_data[key]
