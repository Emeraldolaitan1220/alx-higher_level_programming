#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

"""fetches the url passed as argument"""
def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

"""fetches the url passed as argument"""
if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)