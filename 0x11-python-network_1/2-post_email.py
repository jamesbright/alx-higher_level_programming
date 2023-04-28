#!/usr/bin/python3
""" make a post request and display body of response
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    val = {}
    val['email'] = argv[2]
    data = urlencode(val)
    data = data.encode('utf-8')

    response = Request(url, data)
    with urlopen(response) as res:
        page = res.read().decode('utf-8')
        print(page)
