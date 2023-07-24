#!/usr/bin/env /python3
"""
web file
"""

import requests
import functools
import time

# Decorator to cache the function result with an expiration time of 10 seconds
def cache_with_expiration(expiration_time):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(url):
            # If the cached result exists and not expired, return it
            if url in cache and time.time() - cache[url]["time"] < expiration_time:
                return cache[url]["content"]

            # Fetch the HTML content using requests module
            response = requests.get(url)
            if response.status_code == 200:
                content = response.text
            else:
                content = f"Error: Unable to fetch the page for URL '{url}'"

            # Cache the result along with the current time
            cache[url] = {"content": content, "time": time.time()}

            return content
        return wrapper
    return decorator

# Decorator to track the number of times a URL was accessed
def track_url_access(func):
    access_counts = {}
    @functools.wraps(func)
    def wrapper(url):
        # Increment the access count for the URL
        access_counts[url] = access_counts.get(url, 0) + 1
        return func(url)
    return wrapper

# Apply both decorators to the get_page function
@track_url_access
@cache_with_expiration(expiration_time=10)
def get_page(url: str) -> str:
    return requests.get(url).text

if __name__ == "__main__":
    # Test the get_page function
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"
    for i in range(5):
        content = get_page(url)
        print(f"Access {i + 1} - Content Length: {len(content)}")

    # Wait for 11 seconds to test cache expiration
    time.sleep(11)

    for i in range(5):
        content = get_page(url)
        print(f"Access {i + 1} - Content Length: {len(content)}")

    # Check the number of times the URL was accessed
    print(f"URL '{url}' was accessed {track_url_access.access_counts.get(url, 0)} times.")
