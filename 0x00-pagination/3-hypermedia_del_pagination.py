#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """return correct indexes to paginate the dataset
        """
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)

    def get_page(self, index: int = None, page_size: int = 10) -> List[List]:
        """Returns list with page information form dataset, organized by
        the page number and page size given
        """
        assert isinstance(page_size, int)
        assert type(index) == int
        assert page_size > 0
        assert index >= 0
        data = self.dataset()[index: index + page_size]
        return data

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Method that returns hyper_index dictionary
        """
        assert index >= 0
        assert index < len(self.__dataset)
        num_of_pages = len(self.__dataset) / page_size
        get_index = self.__indexed_dataset.get(index)

        def next_index(index: int, page_size: int) -> Optional[int]:
            """
            Returns next page number or None if no next page
            """
            counter = -1
            for i in range(len(self.__indexed_dataset)):
                if index + i in self.__indexed_dataset:
                    counter += 1
                    if counter == page_size:
                        return index + i

        def hyper_data(index: int, page_size: int) -> List[List]:
            """
            Return list of the data set acording to the list and page
            """
            data_list = []
            counter = 0
            for i in range(len(self.__indexed_dataset)):
                if index + i in self.__indexed_dataset:
                    counter += 1
                    data_list.append(self.__indexed_dataset.get(index + i))
                    if counter == page_size:
                        return data_list

        hyper_index_dict = {
            "index": index,
            "next_index": next_index(index, page_size),
            "page_size": page_size,
            "data": hyper_data(index, page_size)
        }
        return hyper_index_dict


if __name__ == "__main__":
    server = Server()

    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again the initial index -> the first data retreives is not
    # the same as the first request
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as the request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))
