#!/bin/bash
# Takes in a URL, sends a request to the URL
curl -sI "$1" | awk '$1 == "Content-Length:" {print $2}'
