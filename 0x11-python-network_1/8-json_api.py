#!/usr/bin/python3
""" sends data using a post request to http://0.0.0.0:5000/search_user
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        value = sys.argv[1]

    else:
        value = ""
    res = requests.post(url, data={'q': value})
    try:
        json_obj = res.json()
        if not json_obj:
            print("No result")
        else:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
    except ValueError:
        print("Not a valid JSON")
