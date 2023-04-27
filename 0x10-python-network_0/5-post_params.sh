#!/bin/bash
# takes in a URL sends a POST request and displays response body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
