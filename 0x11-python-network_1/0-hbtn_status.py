#!/usr/bin/python3
import urllib.request
"""fetches the value of the X-Request-Id variable"""
def fetch_url():
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("- type: {}".format(type(html)))
        print("- content: {}".format(html))
        print("- utf8 content: {}".format(html.decode('utf-8')))

if __name__ == "__main__":
    fetch_url()