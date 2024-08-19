#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset, resilient to deletions.

        Parameters:
        index (int, optional): The starting index for the page (default is None).
        page_size (int): The number of items per page (default is 10).

        Returns:
        Dict: A dictionary with pagination information.
        """
        # Validate page_size
        assert isinstance(page_size, int) and page_size > 0

        # Get the indexed dataset
        indexed_dataset = self.indexed_dataset()

        # Adjust the index if it is None
        if index is None:
            index = 0

        # Prepare the data to be returned
        data = []
        next_index = index

        # Fetch the requested data
        while len(data) < page_size:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
                next_index += 1
            else:
                # If index is out of range, stop adding data
                break

        # Return the dictionary with pagination info
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
