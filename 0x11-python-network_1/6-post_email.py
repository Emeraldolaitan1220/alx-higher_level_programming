#!/usr/bin/python3
"""sends a POST request to the passed URL with the email"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {
        "email": email
    }
    response = requests.post(url, data=payload)
    print(response.text)
