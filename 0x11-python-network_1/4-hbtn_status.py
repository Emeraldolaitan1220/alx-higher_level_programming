#!/usr/bin/python3
import requests

""" fetch url """
def fetch_url(url):
    response = requests.get(url)
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
""" fetches the url passed as argument """
if __name__ == "__main__":
    fetch_url("https://alx-intranet.hbtn.io/status")