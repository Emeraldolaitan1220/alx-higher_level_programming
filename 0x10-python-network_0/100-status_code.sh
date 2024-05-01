#!/bin/bash
# task 07
curl -s -o /dev/null -I --w "%{http_code}" "$1"
