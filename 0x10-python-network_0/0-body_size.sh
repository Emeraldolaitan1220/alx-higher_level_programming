#!/usr/bin/bash
# This script will check if a file is provided as an argument or not
if [ -z "$1" ]; then
    echo "Usage: $0 <file>"
    exit 1
fi
response=$(curl -s -F "file=@$1" https://file.io)
