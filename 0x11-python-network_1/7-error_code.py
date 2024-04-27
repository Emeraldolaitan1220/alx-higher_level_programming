#!/usr/bin/python3
import requests
import sys

"""displays the body of the response (decoded in utf-8) followed by http status code
"""
def fetch_url(url):
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
"""fetches the url passed as argument"""
if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)