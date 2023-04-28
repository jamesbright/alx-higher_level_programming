#!/usr/bin/python3
""" manage errors and exceptions in request
"""


if __name__ == '__main__':
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as res:
            page = res.read()
            print(page.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
