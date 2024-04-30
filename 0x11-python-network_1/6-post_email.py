#!/usr/bin/python3
import requests
import sys

""" sends a POST request to the passed URL with the 
email as a parameter, and displays the body of the 
response (decoded in utf-8)
"""
def post_email(url, email):
    response = requests.post(url, data = {'email': email})
    print(response.text)

"""main function"""
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)