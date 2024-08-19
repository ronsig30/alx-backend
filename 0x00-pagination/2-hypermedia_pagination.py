#!/usr/bin/env python3
"""
Pagination module for a dataset with hypermedia support.
"""

import csv
import math
from typing import List, Dict, Tuple, Optional


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
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]  # Exclude header
            except FileNotFoundError:
                print(f"File not found: {self.DATA_FILE}")
                raise
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[int]]:

        """
        Get pagination information with hypermedia support.

        Parameters:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

        Returns:
        Dict[str, Optional[int]]: A dictionary with pagination information.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get dataset
        dataset = self.dataset()

        # Calculate total number of pages
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)

        # Get data for the current page
        page_data = self.get_page(page, page_size)

        # Calculate next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return the hypermedia pagination dictionary
        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
