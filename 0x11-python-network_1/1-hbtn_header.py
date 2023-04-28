#!/usr/bin/python3
""" fetch and display X-request-Id
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv

    response = Request(argv[1])
    with urlopen(response) as res:
        xrid_header = res.info()
        print(xrid_header.get('X-Request-Id'))
