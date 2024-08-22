#!/usr/bin/python3
"""
LFU Cache Module
This module implements an LFU (Least Frequently Used) caching system.
"""

from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache implements a caching system using LFU with LRU as a tie-breaker
    ."""
    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = defaultdict(OrderedDict)

    def put(self, key, item):
        """ Add an item to the cache using the LFU algorithm """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing key's value and frequency
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            # Check if cache exceeds max capacity
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()

            # Add the new key and initialize its frequency
            self.cache_data[key] = item
            self._update_frequency(key, initial=True)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency of the accessed key
        self._update_frequency(key)
        return self.cache_data[key]

    def _evict(self):
        """ Evict the least frequently used item """
        # Find the least frequency used
        least_freq = min(self.frequency.values())
        # Find the least recently used key within the least frequency
        least_used_key, _ = self.usage_order[least_freq].popitem(last=False)

        # Remove the key from all tracking structures
        del self.cache_data[least_used_key]
        del self.frequency[least_used_key]
        if not self.usage_order[least_freq]:
            del self.usage_order[least_freq]

        print(f"DISCARD: {least_used_key}")

    def _update_frequency(self, key, initial=False):
        """ Update the frequency and usage order of a key """
        if not initial:
            freq = self.frequency[key]
            del self.usage_order[freq][key]
            if not self.usage_order[freq]:
                del self.usage_order[freq]
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        new_freq = self.frequency[key]
        self.usage_order[new_freq][key] = None
