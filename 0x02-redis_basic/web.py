#!/usr/bin/env python3
"""
Web file
"""
import requests
import datetime

def get_page(url):
    # Check if the cached result exists and has not expired
    cacheKey = f"count:{url}"
    cachedResult = localStorage.getItem(cacheKey)
    cachedTimestamp = localStorage.getItem(f"{cacheKey}:timestamp")
    currentTime = datetime.datetime.now().timestamp() * 1000
    if cachedResult and cachedTimestamp and currentTime - cachedTimestamp <= 10000:
        # Return the cached result
        print(cachedResult)
    else:
        # Make an HTTP request to fetch the HTML content
        response = requests.get(url)
        if response.status_code == 200:
            htmlContent = response.text
            # Cache the result in localStorage
            localStorage.setItem(cacheKey, htmlContent)
            localStorage.setItem(f"{cacheKey}:timestamp", currentTime)
            # Return the fetched HTML content
            print(htmlContent)
        else:
            print(f"Error fetching URL: {response.status_code}")
