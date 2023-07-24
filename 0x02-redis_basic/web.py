#!/usr/bin/env python3
"""
Web file
"""
import requests
import redis
from functools import wraps

# Dictionary to store cached pages
CACHE = {}

def cache_decorator(expiration_time):
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            if url in CACHE and time.time() - CACHE[url]["timestamp"] < expiration_time:
                print(f"Cache hit for {url}")
                return CACHE[url]["content"]

            print(f"Cache miss for {url}")
            content = func(url)
            CACHE[url] = {
                "content": content,
                "timestamp": time.time()
            }
            return content

        return wrapper
    return decorator

@cache_decorator(expiration_time=10)
def get_page(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error fetching page from {url}: {response.status_code}")

# Example usage
if __name__ == "__main__":
    try:
        url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://www.example.com"
        content1 = get_page(url)
        print(content1)

        # Simulate a second request to the same URL within the cache duration
        content2 = get_page(url)
        print(content2)

        # Wait for more than 10 seconds to test cache expiration
        time.sleep(11)

        # The following request should be a cache miss as the cache entry has expired
        content3 = get_page(url)
        print(content3)
        
    except Exception as e:
        print(str(e))
