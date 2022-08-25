#!/usr/bin/env python3
""" class LRUCache inherits from BaseCaching
"""
import operator


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache inherits from BaseCaching and is caching system
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
        LRUCache.COUNTER += 1
        if (key is None or item is None):
            pass
        else:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.counter_dict[key] = LRUCache.COUNTER
            else:
                if key in self.cache_data:
                    self.counter_dict[key] = LRUCache.COUNTER
                    self.cache_data[key] = item
                else:
                    del_key = tuple(sorted(self.counter_dict.items(),
                                    key=operator.itemgetter(1)))[0][0]
                    self.counter_dict.pop(del_key)
                    self.cache_data.pop(del_key)
                    print(f'DISCARD {del_key}')
                    self.counter_dict[key] = LRUCache.COUNTER
                    self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is not None:
            self.counter_dict[key] = LRUCache.COUNTER
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
