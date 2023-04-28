#!/usr/bin/python3
""" fetch a url using urllib
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen


    response = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(response) as f:
        page = f.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('utf8')))
