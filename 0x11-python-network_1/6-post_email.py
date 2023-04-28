#!/usr/bin/python3
""" send a post request with requests
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.post(argv[1], data={'email': argv[2]})
    print(res.text)
