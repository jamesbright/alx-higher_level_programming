#!/bin/bash
# sends a GET request to URL and displays the body of the response
curl -sX GET "$1" -H "X-School-User-Id:98"
