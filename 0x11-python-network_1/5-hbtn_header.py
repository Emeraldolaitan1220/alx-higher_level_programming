#!/usr/bin/python3
import requests
import sys

"""fetches the url passed as argument"""
def fetch_url(url):
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
"""fetches the url passed as argument"""
if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)