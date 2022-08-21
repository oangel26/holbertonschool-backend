#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Method that takes page and page_size args and returns tuple
    containing start_index and end_index corresponding to the range
    of indexes to return in a list for those particular pagination
    parameters
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
