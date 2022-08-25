#!/usr/bin/env python3
""" class MRUCache inherits from BaseCaching
"""
import operator


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache inherits from BaseCaching and is caching system
    """
    COUNTER = 0

    def __init__(self):
        """Initialize cache_data from paretn BaseCaching class. Inheriting
        the dictionary self.chache_data
        """
        super().__init__()
        self.counter_dict = {}

    def put(self, key, item):
        """Assign self.cache_data the item value for the given key.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS discard the least recently used item (LRU algo)
        """
        MRUCache.COUNTER += 1
        if (key is None or item is None):
            pass
        else:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.counter_dict[key] = MRUCache.COUNTER
            else:
                if key in self.cache_data:
                    self.counter_dict[key] = MRUCache.COUNTER
                    self.cache_data[key] = item
                else:
                    del_key = tuple(sorted(self.counter_dict.items(),
                                    key=operator.itemgetter(1))
                                    )[BaseCaching.MAX_ITEMS - 1][0]
                    self.counter_dict.pop(del_key)
                    self.cache_data.pop(del_key)
                    print(f'DISCARD: {del_key}')
                    self.counter_dict[key] = MRUCache.COUNTER
                    self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is not None:
            MRUCache.COUNTER += 1
            self.counter_dict[key] = MRUCache.COUNTER
        return self.cache_data.get(key)
