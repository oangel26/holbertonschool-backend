#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List, Optional, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """return correct indexes to paginate the dataset
        """
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)

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
        """Returns list with page information form dataset, organized by
        the page number and page size given
        """
        assert isinstance(page_size, int)
        assert type(page) == int
        assert page_size > 0
        assert page > 0
        index = self.index_range(page, page_size)
        data = self.dataset()[index[0]: index[1]]
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns dictionary with information about the dataset
        """
        data_size = len(self.dataset())
        total_pages = math.ceil(data_size / page_size)
        data = self.get_page(page, page_size)

        def next_page(page: int, page_size: int) -> Optional[int]:
            """
            Returns next page number or None if no next page
            """
            if (page >= total_pages):
                return None
            return page + 1

        def prev_page(page: int, page_size: int) -> Optional[int]:
            """
            Returns previous ppage number or None if no previous page
            """
            if (page == 1):
                return None
            return page - 1

        hyper_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page(page, page_size),
            'prev_page': prev_page(page, page_size),
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
        return hyper_dict


if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
