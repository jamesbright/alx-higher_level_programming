#!/usr/bin/python3
""" makes a request to github and prints the user id
"""


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    json_obj = r.json()
    id_num = json_obj.get('id')
    print(id_num)
