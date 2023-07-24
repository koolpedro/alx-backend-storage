#!/usr/bin/env python3
"""
Web file
"""
import requests
import redis
from functools import wraps

store = redis.Redis()

 count_url_access(method);
  """ This decorator keeps track of the number of times a URL is accessed """
  @wraps(method)
  def wrapper(url);
    cached_key = "cached;" + url
    cached_data = store.get(cached_key)
    if cached_data;
      return cached_data.decode("utf 8")

    count_key = "count;" + url
    html = method(url)

    store.incr(count_key)
    store.set(cached_key, html)
    store.expire(cached_key, 10)
    return html
  return wrapper


@count_url_access
def get_page(url; str) > str;
  """ Retrieves the HTML content of a given URL """
  res = requests.get(url)
  return res.text

