#!/usr/bin/python3
import requests
import sys
 
""" getting github api"""

def get_github_id(username, token):
    response = requests.get('https://api.github.com/user', auth=(username, token))
    json_response = response.json()
    print(json_response.get('id'))

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)