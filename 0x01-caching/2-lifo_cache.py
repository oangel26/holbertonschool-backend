#!/usr/bin/env python3
""" class LIFOCache inherits from BaseCaching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache inherits from BaseCaching and is caching system
    """
    def __init__(self):
        """Initialize cache_data from paretn BaseCaching class. Inheriting
        the dictionary self.chache_data
        """
        super().__init__()

    def put(self, key, item):
        """Assign self.cache_data the item value for the given key.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS  discard the last item put in cache (LIFO algo).
        """
        if (key is None or item is None):
            pass
        else:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                if key in self.cache_data:
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                else:
                    discard = self.cache_data.popitem()
                    print(f'DISCARD: {discard[0]}')
                    self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key
        """
        if key is None:
            return None
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
