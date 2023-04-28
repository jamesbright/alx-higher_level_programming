#!/usr/bin/python3
""" retrieves and displays a max of 10 github commits
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    res = requests.get(url)
    json_obj = res.json()
    if len(json_obj) <= 10:
        max_com = len(json_obj)
    else:
        max_com = 10
    for num in range(0, max_com):
        commit = json_obj[num]
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(commit.get('sha'), author))
