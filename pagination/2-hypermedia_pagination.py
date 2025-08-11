import csv
import math
from typing import Any, List, Dict



def index_range(page: int, page_size: int) -> tuple:
    return ((page - 1) * page_size, page * page_size)


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
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary with pagination information and data for the requested page.
        Includes page size, current page, data, next/previous page numbers, and total pages.

        Args:
            page (int): Current page number (default: 1)
            page_size (int): Number of items per page (default: 10)

        Returns:
            Dict[str, Any]: Pagination metadata and page data
        """
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)
        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
