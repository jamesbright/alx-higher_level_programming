#!/usr/bin/python3
""" fetch a url with requests
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    print(res.headers.get("X-Request-Id"))
