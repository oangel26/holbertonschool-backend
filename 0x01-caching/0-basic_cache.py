#!/usr/bin/python3
""" BasicCache module which inherits from BaseCaching
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize cache_data from paretn BaseCaching class. Inheriting
        the dictionary self.chache_data
        """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.chache_data the item value for the
        key
        """
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns value of self.cache_data linked to key
        """
        if key is None:
            return None
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
