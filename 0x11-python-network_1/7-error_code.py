#!/usr/bin/python3
""" sends a  request and prints errors if any, else print response body
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
