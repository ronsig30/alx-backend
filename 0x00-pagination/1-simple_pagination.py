#!/usr/bin/env python3
"""
Pagination module for a dataset.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Parameters:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start and end index.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be greater than 0")
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the data for a specific page and page size.

        Parameters:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

        Returns:
        List[List]: The list of rows for the requested page.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get dataset
        dataset = self.dataset()

        # Get index range
        start, end = index_range(page, page_size)

        # Return the correct page
        return dataset[start:end]
