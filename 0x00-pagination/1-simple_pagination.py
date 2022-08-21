#!/usr/bin/env python3
"""
Simple pagination
"""

import requests
import csv
import math
from typing import List, Tuple


""" Downlaod CVS file from URL and save it directory as Popular_Baby_Names.csv

req = requests.get('url with CVS info')
url_content = req.content
csv_file = open('Popular_Baby_Names.csv', 'wb')
csv_file.write(url_content)
csv_file.close()
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """return correct indexes to paginate the dataset
        """
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page_size, int)
        assert type(page) == int
        assert page_size > 0
        assert page > 0
        index = index_range(page, page_size)
        data = self.dataset()[index[0]: index[1]]
        return data


if __name__ == "__main__":

    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))
