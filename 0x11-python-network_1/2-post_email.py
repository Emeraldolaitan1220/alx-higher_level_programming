#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

"""registers an email with a POST request"""
def post_email(url, email):
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

"""main function"""
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
