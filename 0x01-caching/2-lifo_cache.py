#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the LIFOCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using LIFO algorithm
        """
        if key is None or item is None:
            return
 
        if key in self.cache_data:
            # Update the item if the key already exists
            self.cache_data[key] = item
            '''
            Move the key to the end of the order list to mark it as recently  u
            sed
            '''
            self.order.remove(key)
            self.order.append(key)
        else:
            # Add new item to the cache
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the last item (LIFO)
                oldest_key = self.order.pop()
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

            # Add new item to cache
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
