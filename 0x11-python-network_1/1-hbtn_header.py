#!/usr/bin/python3
import urllib.request
import sys

def get_x_request_id(url):
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print("Value of X-Request-Id variable:", x_request_id)
        else:
            print("X-Request-Id variable not found in the response headers.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
