#!/usr/bin/env python3
"""
Web caching module.
"""

import redis
import requests
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def cache_with_expiration(method: Callable) -> Callable:
    """
    Decorator to cache the result of a function with expiration time.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function with caching functionality.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to cache the result of the original function.

        Args:
            url (str): The URL to fetch the page from.

        Returns:
            str: The HTML content of the page.
        """
        # Check if the URL is already cached
        cached_page = redis_client.get(f"cached:{url}")
        if cached_page:
            return cached_page.decode('utf-8')

        # Fetch the page and cache it
        result = method(url)
        redis_client.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


def count_requests(method: Callable) -> Callable:
    """
    Decorator to count the number of requests to a particular URL.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function with request counting functionality.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to count the number of requests
        to the original function.

        Args:
            url (str): The URL to fetch the page from.

        Returns:
            str: The HTML content of the page.
        """
        # Increment the count for the URL
        redis_client.incr(f"count:{url}")
        return method(url)

    return wrapper


@cache_with_expiration
@count_requests
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL.

    Args:
        url (str): The URL to fetch the page from.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.text
