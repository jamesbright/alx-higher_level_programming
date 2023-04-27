#!/bin/bash
# curl and display status code of a request
curl -L -s -X HEAD -w "%{http_code}" "$1"
