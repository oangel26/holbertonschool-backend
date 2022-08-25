#!/usr/bin/env python3
""" class FIFOCache inherits from BaseCaching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache inherits from BaseCaching and is caching system
    """
    def __init__(self):
        """Initialize cache_data from paretn BaseCaching class. Inheriting
        the dictionary self.chache_data
        """
        super().__init__()

    def put(self, key, item):
        """Assign self.cache_data the item value for the given key.
        """
        if (key is None or item is None):
            print("entro a pass")
            pass
        else:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = list(sorted(self.cache_data.keys()))[0]
                print(f'DISCARD: {discard}')
                self.cache_data.pop(list(sorted(self.cache_data.keys()))[0])

    def get(self, key):
        """ Returns the value in self.cache_data linked to key
        """
        if key is None:
            return None
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = FIFOCache()
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
